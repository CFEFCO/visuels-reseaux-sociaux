"""Voix off française de synthèse pour les reels (moteur Kokoro, voix ff_siwis).

Usage :
    python3 outils/voix_off.py "Texte à lire" sortie.mp3 [--vitesse 1.0]
    python3 outils/voix_off.py "Texte à lire" reel_avec_voix.mp4 --video reel.mp4 [--vitesse 1.0] [--debut 0.5]

Au premier lancement, le script installe kokoro-onnx (pip) et télécharge le modèle depuis GitHub
dans ~/.cache/formalaunch-voix. Avec --video, la voix remplace la piste son du reel (la vidéo n'est
pas réencodée) ; --debut décale la voix en secondes. Le son tendance s'ajoute ensuite dans Metricool.
À n'utiliser que si la doc « Ligne éditoriale » indique la voix comme validée par Alexandre.
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

CACHE = Path.home() / ".cache" / "formalaunch-voix"
BASE = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
FICHIERS = ["kokoro-v1.0.int8.onnx", "voices-v1.0.bin"]
VOIX = "ff_siwis"


def preparer():
    try:
        import kokoro_onnx  # noqa: F401
        import soundfile  # noqa: F401
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--break-system-packages",
                        "kokoro-onnx", "soundfile"], check=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    for nom in FICHIERS:
        cible = CACHE / nom
        if not cible.exists() or cible.stat().st_size < 1_000_000:
            subprocess.run(["curl", "-sSL", "-o", str(cible), BASE + nom], check=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("texte")
    p.add_argument("sortie")
    p.add_argument("--video")
    p.add_argument("--vitesse", type=float, default=1.0)
    p.add_argument("--debut", type=float, default=0.0)
    a = p.parse_args()
    preparer()
    import soundfile as sf
    from kokoro_onnx import Kokoro

    k = Kokoro(str(CACHE / FICHIERS[0]), str(CACHE / FICHIERS[1]))
    son, taux = k.create(a.texte, voice=VOIX, speed=a.vitesse, lang="fr-fr")
    wav = Path(tempfile.mkdtemp()) / "voix.wav"
    sf.write(wav, son, taux)
    duree = len(son) / taux
    if a.video:
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-i", a.video, "-itsoffset", str(a.debut), "-i", str(wav),
            "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
            "-af", "apad", "-shortest", "-movflags", "+faststart", a.sortie,
        ], check=True)
    else:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-c:a", "libmp3lame",
                        "-b:a", "128k", a.sortie], check=True)
    print(f"OK {a.sortie} : voix de {duree:.1f} s")


if __name__ == "__main__":
    main()

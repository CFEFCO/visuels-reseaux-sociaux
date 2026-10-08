# visuels-reseaux-sociaux

Visuels des publications Instagram, programmées ensuite dans Metricool. Une marque par dossier (Formalaunch pour commencer).

Ce dépôt est **public** : n'y déposer que des visuels validés, juste avant leur programmation.

## Organisation

| Dossier | Contenu |
|---|---|
| `outils/rendu_png.py` | Transforme un visuel HTML (ou un gabarit du canvas) en PNG |
| `outils/polices/` | Police Poppins (licence OFL, voir `OFL.txt`) |
| `formalaunch/logos/` | Logos Formalaunch, nommés par leur identifiant dans le canvas des gabarits |
| `formalaunch/AAAA-MM/` | Visuels validés du mois (ex. `formalaunch/2026-11/`) |

## Rendu d'un visuel

```
python3 outils/rendu_png.py visuel.html visuel.png 1080 1350
python3 outils/rendu_png.py story.html story.png 1080 1920
python3 outils/rendu_png.py couverture.dc.html couverture.png 1080 1350 fond=#005486
```

## Lien public d'un visuel

`https://raw.githubusercontent.com/CFEFCO/visuels-reseaux-sociaux/main/<chemin du fichier>`

Metricool récupère l'image à partir de ce lien au moment de la programmation et en garde sa propre copie.

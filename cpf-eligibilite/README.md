# cpf-eligibilite.fr : nouvelle version

Page d'accueil refaite pour les campagnes Google Ads (bilan de compétences financé par le CPF).
Site statique, sans WordPress : `index.html` + `mentions-legales.html` + `robots.txt` + `sitemap.xml`.

## Urgent : le site actuel est piraté

Au 9 novembre 2026, la page d'accueil WordPress contient des liens cachés vers des sites de casino et de paris
(`bonusdebienvenue-casinos.com`, `staging.dawnsol.com` « judi bola / sbobet », `nusantarabola.id`).
Google peut classer le site comme « compromis » : annonces refusées et pénalité SEO.

1. Changer tous les mots de passe (WordPress, hébergeur, FTP, base de données).
2. Supprimer les extensions et thèmes inutilisés, mettre à jour le reste.
3. Remplacer le site par cette version statique (aucun WordPress, donc plus rien à pirater).
4. Dans Google Search Console : vérifier « Problèmes de sécurité », puis demander un réexamen si besoin.

## À compléter avant la mise en ligne

Les zones surlignées en jaune (`class="todo"`) dans le pied de page et dans `mentions-legales.html` :
raison sociale, adresse, SIRET, numéro de déclaration d'activité (NDA), région, n° de certificat Qualiopi,
hébergeur, e-mail de contact, lien vers les CGV.

À vérifier dans le contenu :
- **4,82/5 et 10 000 bénéficiaires** : à garder seulement si vous pouvez le prouver (avis Google, Trustpilot,
  bilans Qualiopi). Sinon, Google Ads peut refuser les annonces pour « affirmations non vérifiables ».
- **Entretien de suivi à 6 mois** et **durées des phases (3 h / 18 h / 3 h)** : à ajuster à votre programme réel.
- **Logo Qualiopi** : ajouter le logo officiel (fichier fourni par votre certificateur) à côté de la mention.

## Suivi des conversions Google Ads

- Coller le tag Google (gtag.js) à l'endroit indiqué dans le `<head>` de `index.html`.
- Ajouter un bandeau cookies compatible Consent Mode v2 (obligatoire en France pour les tags Google Ads).
- Chaque bouton porte un attribut `data-cta` (`header`, `hero`, `situations`, `final`, `mobile-bar`) pour suivre les clics.
- Typeform : configurer une redirection de fin vers une page de remerciement du site (ex. `/merci.html`)
  et déclencher la conversion Google Ads sur cette page. C'est la mesure la plus fiable.

## Règles CPF prises en compte dans les textes

- Participation forfaitaire obligatoire de 150 € depuis le 2 avril 2026 (décret n° 2026-234), affichée clairement.
- Plafond CPF du bilan de compétences : 1 600 € depuis le 26 février 2026.
- Le bilan n'est pas concerné par la majoration prévue au PLF 2027 (source : moncompteformation.gouv.fr).
- Pas de mot « gratuit » pour le bilan, pas de cadeau, rappel que personne ne doit demander les identifiants CPF.
- Mention « organisme privé, non affilié à Mon Compte Formation » : le nom de domaine contient « CPF »,
  cette mention évite toute confusion avec le service officiel.
- Anciennes mentions « Datadock » et « OPCA » supprimées (remplacés par Qualiopi en 2022 et les OPCO en 2019).

## Mise en ligne

Déposer le contenu du dossier à la racine de l'hébergement (ou sur Netlify, Vercel, OVH…), puis :
- soumettre `sitemap.xml` dans Google Search Console ;
- vérifier que `https://cpf-eligibilite.fr/` charge bien `index.html` ;
- rediriger les anciennes URL WordPress (301) vers la page d'accueil.

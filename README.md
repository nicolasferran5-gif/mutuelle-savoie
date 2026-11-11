# mutuelle-savoie.fr · Bonne Cordée

Site satellite de WealthWise Conseil pour les entreprises de montagne de Savoie et Haute-Savoie (stations, hôtels-restaurants IDCC 1979, remontées mécaniques IDCC 454, saisonniers, indépendants).

- Sources : `_build/` (moteur commun `build.py`, identité `site.py`, pages `pages.py`, articles `articles.py`). Publication d'un article : voir `_build/PUBLIER.md`.
- Génération : `python3 _build/build.py deploy /tmp/sv-out && cp -r /tmp/sv-out/. .`
- Hébergement : Vercel (déploiement automatique depuis `main`).

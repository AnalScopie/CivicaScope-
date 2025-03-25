# CivicaScope – API citoyenne intelligente

CivicaScope est une application FastAPI qui permet d’analyser des données locales (logement, emploi, écologie, etc.) et de générer automatiquement des discours ou revendications citoyennes, adaptées à différents styles (solennel, fédérateur, sémantique).

## Technologies
- Python 3.10+
- FastAPI
- Uvicorn
- OpenAI (en option)
- Déploiement via Render

## Fichiers
- `main.py` : code principal de l’API
- `requirements.txt` : dépendances Python
- `Procfile` : configuration Render
- `README.md` : documentation du projet

## Lancement local (optionnel)
```bash
pip install -r requirements.txt
uvicorn main:app --reload

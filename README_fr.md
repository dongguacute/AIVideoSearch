# Recherche Vidéo IA

[English](README.md) | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Español](README_es.md)

---

Utilisez l'API IA pour décrire et rechercher des vidéos. Il suffit de télécharger une vidéo et de rechercher par description.

## Installation
1. Clonez le projet :
   ```bash
   git clone https://github.com/yourname/AIVideoSearch.git
   cd AIVideoSearch
   ```
2. Installez les dépendances via pyproject.toml avec uv :
   ```bash
   uv pip install -r pyproject.toml
   ```
3. Définissez votre clé API dans `src/setting.env` (remplissez votre propre clé API IA) :
   ```env
   API_KEY=your-api-key
   ```

## Démarrage
Lancez le backend :
```bash
python3 -m src.main
```
Ouvrez `test/index.html` dans votre navigateur pour le frontend.

## Licence
MIT
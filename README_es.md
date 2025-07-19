# Búsqueda de Videos con IA

[English](README.md) | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Español](README_es.md)

---

Utiliza la API de IA para describir y buscar videos. Simplemente sube un video y búscalo por descripción.

## Instalación
1. Clona el proyecto:
   ```bash
   git clone https://github.com/yourname/AIVideoSearch.git
   cd AIVideoSearch
   ```
2. Instala las dependencias usando pyproject.toml con uv:
   ```bash
   uv pip install -r pyproject.toml
   ```
3. Configura tu clave API en `src/setting.env` (rellena tu propia clave de IA):
   ```env
   API_KEY=your-api-key
   ```

## Inicio
Ejecuta el backend:
```bash
python3 -m src.main
```
Abre `test/index.html` en tu navegador para el frontend.

## Licencia
MIT
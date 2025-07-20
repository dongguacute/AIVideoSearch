# AI Video Search

[English](README.md) | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Español](README_es.md)

---

Use AI API to describe and search videos. Simply upload a video and search by description.

## Installation
1. Clone the project:
   ```bash
   git clone https://github.com/dongguacute/AIVideoSearch.git
   cd AIVideoSearch
   ```
2. Install dependencies via pyproject.toml with uv:
   ```bash
   uv pip install -r pyproject.toml
   ```
3. Set your API key in `src/setting.env` (please fill in your actual AI API key):
   ```env
   API_KEY=your-api-key
   ```

## Start
Run backend:
```bash
python3 -m src.main
```
Open `test/index.html` in your browser for the frontend.

## License
MIT

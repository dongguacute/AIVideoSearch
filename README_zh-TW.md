# AI 影片搜尋

[English](README.md) | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Español](README_es.md)

---

使用AI API描述並搜尋影片。只需上傳影片，即可透過描述進行搜尋。

## 安裝
1. 複製專案：
   ```bash
   git clone https://github.com/dongguacute/AIVideoSearch.git
   cd AIVideoSearch
   ```
2. 透過pyproject.toml使用uv安裝依賴：
   ```bash
   uv pip install -r pyproject.toml
   ```
3. 在 `src/setting.env` 設定你的API金鑰（請填寫實際AI API金鑰）：
   ```env
   API_KEY=your-api-key
   ```

## 啟動
執行後端：
```bash
python3 -m src.main
```
前端請在瀏覽器開啟 `test/index.html`。

## 協議
MIT

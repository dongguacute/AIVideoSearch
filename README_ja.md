# AI動画検索

[English](README.md) | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Español](README_es.md)

---

AI APIを使って動画を記述・検索できます。動画をアップロードし、説明文で検索できます。

## インストール
1. プロジェクトをクローン：
   ```bash
   git clone https://github.com/dongguacute/AIVideoSearch.git
   cd AIVideoSearch
   ```
2. pyproject.tomlを使ってuvで依存関係をインストール：
   ```bash
   uv pip install -r pyproject.toml
   ```
3. `src/setting.env` にAPIキーを設定（ご自身のAI APIキーを入力してください）：
   ```env
   API_KEY=your-api-key
   ```

## 起動
バックエンドを起動：
```bash
python3 -m src.main
```
フロントエンドはブラウザで `test/index.html` を開いてください。

## ライセンス
MIT
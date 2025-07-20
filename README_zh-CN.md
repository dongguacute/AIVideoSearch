# AI 视频搜索

[English](README.md) | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Español](README_es.md)

---

使用AI API描述并搜索视频。只需上传视频，即可通过描述进行搜索。

## 安装
1. 克隆项目：
   ```bash
   git clone https://github.com/dongguacute/AIVideoSearch.git
   cd AIVideoSearch
   ```
2. 通过pyproject.toml使用uv安装依赖：
   ```bash
   uv pip install -r pyproject.toml
   ```
3. 在 `src/setting.env` 设置你的API密钥（请填写实际AI API密钥）：
   ```env
   API_KEY=your-api-key
   ```

## 启动
运行后端：
```bash
python3 -m src.main
```
前端请在浏览器打开 `test/index.html`。

## 协议
MIT

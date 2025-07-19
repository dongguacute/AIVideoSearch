"""
app.py
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import aiofiles
from .config import get_ai_api_key
import httpx
from fastapi import Query
import glob
import os
from fastapi.middleware.cors import CORSMiddleware
import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/post_video")
async def post_video(request: Request):
    logging.info("Received /post_video request")
    data = await request.json()
    video_title = data.get("video_title", "")
    video_description = data.get("video_description", "")
    video_cc = data.get("video_cc", "")
    video_path = data.get("video_path", "")
    logging.info(f"Title: {video_title}, Description: {video_description}, Path: {video_path}, CC Length: {len(video_cc)}")
    prompt = f"Please analyze these texts and summarize them into a long paragraph. Do not end with a period. Only output the content, do not output any useless information. Title: {video_title}\nDescription: {video_description}\nCC: {video_cc}"
    api_key = get_ai_api_key()
    if not api_key:
        logging.error("AI_API_KEY not found.")
        return JSONResponse(status_code=500, content={"error": "AI_API_KEY not found."})
    # OpenRouter API
    url = "YOUR API URL"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "X-Title": "AIVideoSearch"
    }
    data = {
        "model": "YOUR MODEL NAME",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    logging.info("Start requesting API...")
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
        logging.info(f"API response code: {response.status_code}")
        if response.status_code != 200:
            try:
                error_detail = response.json()
            except Exception:
                error_detail = response.text
            logging.error(f"API request failed: {error_detail}")
            return JSONResponse(status_code=500, content={"error": f"OpenRouter API request failed: {error_detail}"})
        result = response.json()
        ai_summary = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        if not ai_summary:
            logging.error("API did not return a summary.")
            return JSONResponse(status_code=500, content={"error": "OpenRouter API did not return a summary."})
        # Truncate summary to avoid overly long filenames
        safe_summary = ai_summary[:60].replace("/", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace("\"", "_").replace("<", "_").replace(">", "_").replace("|", "_")
        # Ensure search directory exists
        os.makedirs("search", exist_ok=True)
        filename = os.path.join("search", f"{safe_summary}.pwq")
        async with aiofiles.open(filename, "w", encoding="utf-8") as f:
            await f.write(video_path)
        logging.info(f"Summary saved: {filename}")
        return {"summary": ai_summary, "pwq_file": filename}

@app.get("/search")
async def search_videos(keyword: str = Query(..., description="Keyword to search in summary filenames")):
    """
    Search for .pwq files whose filenames (AI summary) contain the keyword or any character in the keyword.
    Returns a list of matched video storage paths.
    """
    matched_files = []
    search_dir = "search"
    if not os.path.exists(search_dir):
        return matched_files
    for file in glob.glob(os.path.join(search_dir, "*.pwq")):
        filename = os.path.basename(file)[:-4].lower()
        if any(char in filename for char in keyword.lower()):
            async with aiofiles.open(file, "r", encoding="utf-8") as f:
                video_path = await f.read()
                matched_files.append({"summary": os.path.basename(file)[:-4], "video_path": video_path})
    return matched_files
    

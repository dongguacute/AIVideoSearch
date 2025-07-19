"""
main.py
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .app import app
from . import base
import uvicorn

@app.get("/")
async def read_root():
    return {"message": "Welcome use AI Video Search"}

if __name__ == "__main__":
    base.logoprint()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )

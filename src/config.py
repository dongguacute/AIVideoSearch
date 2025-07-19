import os

def get_ai_api_key(env_path="/Users/gudupao/Downloads/AIVideoSearch/src/setting.env"):
    """
    Read the value of AI_API_KEY from the specified setting.env file.
    Return None if not found.
    """
    if not os.path.exists(env_path):
        return None
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("AI_API_KEY="):
                return line.split("=", 1)[1]
    return None

from fastapi import APIRouter, HTTPException
import subprocess

social_media_module = APIRouter()

@social_media_module.post("/post")
def post_to_social_media(platform: str, content: str, media_file: str = None):
    try:
        output_message = f"Posted to {platform} successfully!"
        subprocess.run(["python", "scripts/social_media.py", "--platform", platform, "--content", content, "--media", media_file])
        return {"message": output_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

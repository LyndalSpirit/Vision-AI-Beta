from fastapi import APIRouter, HTTPException
import subprocess

avatar_lipsync_module = APIRouter()

@avatar_lipsync_module.post("/")
def generate_lip_sync(audio_file: str, avatar_image: str):
    try:
        output_path = "generated_lip_sync.mp4"
        subprocess.run(["python", "scripts/sadtalker.py", "--audio", audio_file, "--image", avatar_image, "--output", output_path])
        return {"message": "Lip sync video created successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

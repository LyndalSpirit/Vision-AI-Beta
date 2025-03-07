from fastapi import APIRouter, HTTPException
import subprocess

video_lipsync_module = APIRouter()

@video_lipsync_module.post("/")
def generate_video_lip_sync(audio_file: str, video_file: str):
    try:
        output_path = "generated_video_lip_sync.mp4"
        subprocess.run(["python", "scripts/video_lipsync.py", "--audio", audio_file, "--video", video_file, "--output", output_path])
        return {"message": "Lip sync applied to video successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

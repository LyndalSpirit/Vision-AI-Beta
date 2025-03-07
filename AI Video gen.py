from fastapi import APIRouter, HTTPException
import subprocess

video_generation_module = APIRouter()

@video_generation_module.post("/")
def generate_video(prompt: str):
    try:
        output_path = "generated_video.mp4"
        subprocess.run(["python", "scripts/animatediff.py", "--prompt", prompt, "--output", output_path])
        return {"message": "Video generated successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

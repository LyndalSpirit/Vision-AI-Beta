from fastapi import APIRouter, HTTPException
import subprocess

image_generation_module = APIRouter()

@image_generation_module.post("/")
def generate_image(prompt: str):
    try:
        output_path = "generated_image.png"
        subprocess.run(["python", "scripts/stable_diffusion.py", "--prompt", prompt, "--output", output_path])
        return {"message": "Image generated successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

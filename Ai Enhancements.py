from fastapi import APIRouter, HTTPException
import subprocess

enhancement_module = APIRouter()

@enhancement_module.post("/")
def enhance_image(image_file: str):
    try:
        output_path = "enhanced_image.png"
        subprocess.run(["python", "scripts/enhance.py", "--input", image_file, "--output", output_path])
        return {"message": "Image enhanced successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

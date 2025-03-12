from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import subprocess
import os

# Initialize FastAPI app
app = FastAPI()

# Load the local GPT model (example using Mistral or GPT-4-All)
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        input_ids = tokenizer.encode(request.message, return_tensors="pt").to("cuda")
        output = model.generate(input_ids, max_length=100)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "AI Avatar Backend is running!"}

# Image Generation Endpoint using Stable Diffusion
@app.post("/generate_image")
def generate_image(prompt: str):
    try:
        output_path = "generated_image.png"
        subprocess.run(["python", "scripts/stable_diffusion.py", "--prompt", prompt, "--output", output_path])
        return {"message": "Image generated successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Video Generation Endpoint using AnimateDiff
@app.post("/generate_video")
def generate_video(prompt: str):
    try:
        output_path = "generated_video.mp4"
        subprocess.run(["python", "scripts/animatediff.py", "--prompt", prompt, "--output", output_path])
        return {"message": "Video generated successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Lip Sync Generation using SadTalker
@app.post("/lip_sync")
def lip_sync(audio_file: str, avatar_image: str):
    try:
        output_path = "lip_sync_video.mp4"
        subprocess.run(["python", "scripts/sadtalker.py", "--audio", audio_file, "--image", avatar_image, "--output", output_path])
        return {"message": "Lip sync video created successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Flux AI Integration for Advanced AI Processing
@app.post("/flux_ai")
def flux_ai_process(task: str, data: str):
    try:
        output_path = "flux_ai_output.json"
        subprocess.run(["python", "scripts/flux_ai.py", "--task", task, "--data", data, "--output", output_path])
        return {"message": "Flux AI processing complete!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Anime Image Processing using Stable Diffusion Anime Models
@app.post("/generate_anime_image")
def generate_anime_image(prompt: str):
    try:
        output_path = "generated_anime_image.png"
        subprocess.run(["python", "scripts/stable_diffusion_anime.py", "--prompt", prompt, "--output", output_path])
        return {"message": "Anime-style image generated successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Anime Video Processing using AnimeGAN or AI-Based Models
@app.post("/generate_anime_video")
def generate_anime_video(prompt: str):
    try:
        output_path = "generated_anime_video.mp4"
        subprocess.run(["python", "scripts/animegan_video.py", "--prompt", prompt, "--output", output_path])
        return {"message": "Anime-style video generated successfully!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

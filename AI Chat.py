from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

chat_module = APIRouter()

# Load the local GPT model
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")

class ChatRequest(BaseModel):
    message: str

@chat_module.post("/")
def chat(request: ChatRequest):
    try:
        input_ids = tokenizer.encode(request.message, return_tensors="pt").to("cuda")
        output = model.generate(input_ids, max_length=100)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

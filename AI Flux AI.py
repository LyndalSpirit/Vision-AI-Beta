from fastapi import APIRouter, HTTPException
import subprocess

flux_ai_module = APIRouter()

@flux_ai_module.post("/")
def flux_ai_process(task: str, data: str):
    try:
        output_path = "flux_ai_output.json"
        subprocess.run(["python", "scripts/flux_ai.py", "--task", task, "--data", data, "--output", output_path])
        return {"message": "Flux AI processing complete!", "file": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter, HTTPException
import os
import json

project_module = APIRouter()
PROJECTS_DIR = "projects/"

# Ensure projects directory exists
os.makedirs(PROJECTS_DIR, exist_ok=True)

@project_module.post("/create")
def create_project(name: str, description: str = ""):
    try:
        project_path = os.path.join(PROJECTS_DIR, f"{name}.json")
        if os.path.exists(project_path):
            raise HTTPException(status_code=400, detail="Project already exists.")
        
        project_data = {"name": name, "description": description, "files": []}
        with open(project_path, "w") as f:
            json.dump(project_data, f)
        
        return {"message": "Project created successfully!", "project": project_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@project_module.get("/list")
def list_projects():
    try:
        projects = [f.replace(".json", "") for f in os.listdir(PROJECTS_DIR) if f.endswith(".json")]
        return {"projects": projects}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@project_module.post("/add_file")
def add_file_to_project(project_name: str, file_name: str):
    try:
        project_path = os.path.join(PROJECTS_DIR, f"{project_name}.json")
        if not os.path.exists(project_path):
            raise HTTPException(status_code=404, detail="Project not found.")
        
        with open(project_path, "r+") as f:
            project_data = json.load(f)
            if file_name in project_data["files"]:
                raise HTTPException(status_code=400, detail="File already exists in project.")
            project_data["files"].append(file_name)
            f.seek(0)
            json.dump(project_data, f)
            f.truncate()
        
        return {"message": "File added successfully!", "project": project_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

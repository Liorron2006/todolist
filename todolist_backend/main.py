from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from db import get_all_tasks, create_task, update_task, delete_task, delete_all_tasks, update_task_image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tasks")
def read_tasks():
    return get_all_tasks()

@app.post("/tasks")
async def add_task(request: Request):
    data = await request.json()
    return create_task(data["title"])

@app.put("/tasks/{task_id}")
async def edit_task(task_id: str, request: Request):
    data = await request.json()
    return update_task(task_id, data["title"])

@app.delete("/tasks/{task_id}")
def remove_task(task_id: str):
    return delete_task(task_id)

@app.delete("/tasks")
def remove_all_tasks():
    return delete_all_tasks()

@app.post("/tasks/{task_id}/image")
async def add_image(task_id: str, request: Request):
    data = await request.json()
    return update_task_image(task_id, data["image_url"])

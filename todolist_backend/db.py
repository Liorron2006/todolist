from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.todo_db
collection = db.tasks

def get_all_tasks():
    tasks = list(collection.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

def create_task(title):
    task = {"title": title, "image_url": ""}
    result = collection.insert_one(task)
    task["_id"] = str(result.inserted_id)
    return task

def update_task(task_id, new_title):
    collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"title": new_title}})
    return {"_id": task_id, "title": new_title}

def delete_task(task_id):
    collection.delete_one({"_id": ObjectId(task_id)})
    return {"_id": task_id}

def delete_all_tasks():
    collection.delete_many({})
    return {"message": "All tasks deleted"}

def update_task_image(task_id, image_url):
    collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"image_url": image_url}})
    return {"_id": task_id, "image_url": image_url}

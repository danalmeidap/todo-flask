from __future__ import annotations
from datetime import datetime
from app.database import mongo
from typing import Any


def get_all_tasks(active:bool= True) ->dict:
    tasks = [task for task in mongo.db.tasks.find({"active": active})]
    return tasks
                      

def get_tasks_by_user(user:str, active:bool= True) ->dict:
    user_tasks= [task for task in mongo.db.tasks.find({"user":user})]
    return user_tasks

def get_task_by_slug(slug:str) ->dict:
    task = mongo.db.tasks.find_one({"slug":slug})
    return task


def update_task_by_slug(user:str, slug:str, data)->str:
    return mongo.db.tasks.find_one_and_update({"user":user}, {"slug":slug}, {"$set":data})


def new_task(user:str, title:str, content:str, active:bool=True) ->str:
    slug = title.replace("_","-").replace(" ", "-").lower()
    new = mongo.db.tasks.insert_one(
        {
            "user":user,
            "title":title,
            "content":content,
            "slug":slug,
            "active":active,
            "date":datetime.now()
        }
    )
    return slug






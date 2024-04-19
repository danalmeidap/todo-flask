from __future__ import annotations
from datetime import datetime
from app.database import mongo
import pymongo
from typing import Any


def get_all_tasks(active:bool= True) -> list[dict[str, Any]]:
    tasks = mongo.db.tasks.find({"active": active})
    return tasks.sort("date", pymongo.DESCENDING)


def get_tasks_by_user(user:str) ->list[dict[str, Any]]:
    user_tasks=mongo.db.tasks.find({{"user":user}, {"active":True}})
    return user_tasks.sort("date", pymongo.DESCENDING)


def get_task_by_slug(slug:str) ->dict[str, Any]:
    task = mongo.db.tasks.find_one({"slug":slug})
    return task


def update_task_by_name(user:str, name:str, data:dict[str, Any])->str:
    return mongo.db.tasks.find_one_and_update({"slug":user}, {"name":name}, {"$set":data})


def new_task(user:str, title:str, content:str, active:bool=True) ->str:
    slug = title.replace("_","-").replace(" ", "-").lower()
    new = mongo.db.tasks.insert_one(
        {
            "user":user,
            "title":title,
            "content":content,
            "slug":slug,
            "date":datetime.now()
        }
    )
    return slug






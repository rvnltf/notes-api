import datetime
from typing import Union
from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse
from config.database import collection_name
from models.notesModel import Note
from schemas.notesSchema import note_serialize, notes_serialize
from bson import ObjectId
import re

note_api_router = APIRouter()

#redirect root path to docs
@note_api_router.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')

#retrieve
@note_api_router.get("/")
async def get_notes():
    notes = notes_serialize(collection_name.find())
    return {"success": True, "data": notes}

@note_api_router.get("/{id}")
async def get_note(id: str):
    note = notes_serialize(collection_name.find({"_id": ObjectId(id)}))
    return {"success": True, "data": note}

@note_api_router.get("/user/{user}")
async def get_note(user: str):
    note = notes_serialize(collection_name.find({"user":user}))
    return {"success": True, "data": note}

#insert
@note_api_router.post("/")
async def post_note(note: Note):
    date = {'createdAt': datetime.datetime.now(), 'updatedAt':  datetime.datetime.now()}
    data = dict(note)
    data.update(date)
    _id = collection_name.insert_one(data)
    note = notes_serialize(collection_name.find({"_id": _id.inserted_id}))
    return {"success": True, "data": note}

#update
@note_api_router.put("/{id}")
async def put_note(id: str, note: Note):
    date = {'updatedAt':  datetime.datetime.now()}
    data = dict(note)
    data.update(date)
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": data
    })
    note = notes_serialize(collection_name.find({"_id": ObjectId(id)}))
    return {"success": True, "data": note}

#delete
@note_api_router.delete("/{id}")
async def delete_note(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"success": True, "data": []}

#find regex
@note_api_router.get("/find/{keywords}",    
    summary="Find notes by keywords",
    description="Find notes by multiple word(s) using regex regardless of position")
#async def find_note(keywords: str | None = Query(None, description="My description")):
async def find_note(keywords: Union[str, None] = Query(Default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match")):
    #print(keywords)

    strs = keywords.split()
    prefix = "^"
    suffix = ".*$"
    #print(strs)

    search_key = prefix
    for x in strs:
        search_key += "(?=.*\\b" + x + "\\b)"
        #search_key += "(?=.*" + x + ")"
        #print(x)
    search_key += suffix
    #print(search_key)

    regx = re.compile(search_key, re.IGNORECASE)
    notes = notes_serialize(collection_name.find({"text": regx}))
    #print(note) 

    return {"success": True, "data": notes}

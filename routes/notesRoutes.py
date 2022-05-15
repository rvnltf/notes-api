import datetime
from fastapi import APIRouter
from config.database import collection_name
from models.notesModel import Note
from schemas.notesSchema import note_serialize, notes_serialize
from bson import ObjectId

note_api_router = APIRouter()

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
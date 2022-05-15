from fastapi import FastAPI
from routes.notesRoutes import note_api_router

app = FastAPI()

app.include_router(note_api_router)
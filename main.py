from fastapi import FastAPI
from routes.notesRoutes import note_api_router

app = FastAPI(
    title="NOTE API",
    description="This API was built as a final project for PROA KOMINFO PYTHON."
    )

app.include_router(note_api_router)
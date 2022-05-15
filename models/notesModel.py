from datetime import datetime
from pydantic import BaseModel

class Note(BaseModel):
    title: str
    text: str
    user: str
    # createdAt: datetime
    # updatedAt: datetime
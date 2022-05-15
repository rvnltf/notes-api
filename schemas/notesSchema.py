def note_serialize(note) -> dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "text": note["text"],
        "user": note["user"],
        "createdAt": note["createdAt"],
        "updatedAt": note["updatedAt"]
    }

def notes_serialize(notes) -> list:
    return [note_serialize(note) for note in notes]
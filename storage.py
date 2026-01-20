import json
from note import Note

FILE_NAME = "notes.json"


def save_notes(notes):
    """Save list of Note objects to JSON file"""
    with open(FILE_NAME, "w") as f:
        json.dump([note.save() for note in notes], f, indent=2)


def load_notes():
    """Load notes from JSON file"""
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            notes = []
            for item in data:
                note = Note(
                    item["title"],
                    item["content"],
                    item["tags"]
                )
                note.timestamp = item["timestamp"]
                notes.append(note)
            return notes
    except (FileNotFoundError, json.JSONDecodeError):
        return []

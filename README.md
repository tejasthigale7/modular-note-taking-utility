# 🗒️ Modular Note-Taking Utility (Python)

A fully modular **command-line note-taking application** built using Python.  
This project demonstrates **Object-Oriented Programming (OOP)**, **file persistence using JSON**, and **clean modular design**.

Notes are automatically saved and reloaded when the program restarts.

---

## 🚀 Features

- Add notes with title, content, tags, and timestamp
- View all notes in formatted output
- Search notes by keyword or tag
- Delete notes by index
- Persistent storage using JSON (`notes.json`)
- Auto-reload notes on program restart
- Robust error handling for missing or corrupt files
- Clean, menu-driven CLI interface

---

## 🧠 Concepts Used

- Object-Oriented Programming (Classes & Objects)
- Encapsulation
- Modular programming
- File I/O with JSON
- Exception handling
- Lists and dictionaries
- Datetime handling

---

## 📂 Project Structure

modular-note-taking-utility/
│
├── note.py # Defines the Note class
├── storage.py # Save/load notes from JSON
├── main.py # CLI entry point
├── notes.json # Persistent storage (auto-created)
├── README.md
└── .gitignore

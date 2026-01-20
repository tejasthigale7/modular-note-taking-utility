from note import Note
from storage import save_notes, load_notes


def display_menu():
    print("\n=== Note Manager ===")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Exit")


def add_note(notes):
    title = input("Enter title: ").strip()
    content = input("Enter content: ").strip()
    tags_input = input("Enter tags (comma separated): ")
    tags = [t.strip() for t in tags_input.split(",") if t.strip()]

    note = Note(title, content, tags)
    notes.append(note)
    save_notes(notes)
    print("Note added successfully.")


def view_notes(notes):
    if not notes:
        print("No notes available.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"\nNote #{i}")
        note.display()


def search_notes(notes):
    term = input("Enter keyword or tag to search: ").strip()
    results = [note for note in notes if note.matches_search(term)]

    if not results:
        print("No matching notes found.")
    else:
        for note in results:
            note.display()


def delete_note(notes):
    view_notes(notes)
    if not notes:
        return

    try:
        index = int(input("Enter note number to delete: "))
        if 1 <= index <= len(notes):
            del notes[index - 1]
            save_notes(notes)
            print("Note deleted.")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    notes = load_notes()
    print("Notes loaded successfully.")

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

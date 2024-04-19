import json
import os
from datetime import datetime

NOTES_FILE = 'notes.json'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def delete_note():
    note_id = int(input("Введите номер заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с таким номером не найдена")

def list_notes():
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['timestamp']}")
        print(f"Тело: {note['body']}")
        print()

def main():
    global notes
    notes = load_notes()

    while True:
        command = input("Введите команду (add, delete, list, exit): ").strip().lower()

        if command == 'add':
            add_note()
        elif command == 'delete':
            delete_note()
        elif command == 'list':
            list_notes()
        elif command == 'exit':
            break
        else:
            print("Некорректная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()

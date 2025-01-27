def save_notes_to_file(notes, filename):
    with open(filename, 'w') as file:
        for note in notes:
            file.write(f"Имя пользователя: {note['username']}\n")
            file.write(f"Заголовок: {note['title']}\n")
            file.write(f"Описание: {note['content']}\n")
            file.write(f"Статус: {note['status']}\n")
            file.write(f"Дата создания: {note['created_date']}\n")
            file.write(f"Дедлайн: {note['issue_date']}\n")
            file.write("---" + "\n\n")  # Разделитель между заметками


# Пример использования
if __name__ == "__main__":
    notes = [
        {
            "username": "Иван",
            "title": "Заметка 1",
            "content": "Это первая заметка.",
            "status": "Новая",
            "created_date": "2023-10-01",
            "issue_date": "2023-11-30"
        },
        {
            "username": "Петр",
            "title": "Заметка 2",
            "content": "Это вторая заметка.",
            "status": "В процессе",
            "created_date": "2023-09-25",
            "issue_date": "2023-12-15"
        }
    ]

    save_notes_to_file(notes, "notes.txt")

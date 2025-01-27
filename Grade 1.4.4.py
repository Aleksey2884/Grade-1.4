def append_notes_to_file(notes, filename):
    try:
        with open(filename, 'a') as file:
            for note in notes:
                file.write(f"\nИмя пользователя: {note['username']}\n")
                file.write(f"Заголовок: {note['title']}\n")
                file.write(f"Описание: {note['content']}\n")
                file.write(f"Статус: {note['status']}\n")
                file.write(f"Дата создания: {note['created_date']}\n")
                file.write(f"Дедлайн: {note['issue_date']}\n")
                file.write("---" + "\n\n")  # Разделитель между заметками

    except IOError as e:
        print(f"Произошла ошибка при добавлении заметок в файл {filename}: {e}")

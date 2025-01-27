def save_notes_to_file(notes, filename):
    try:
        with open(filename, 'w') as file:
            for note in notes:
                file.write(f"Имя пользователя: {note['username']}\n")
                file.write(f"Заголовок: {note['title']}\n")
                file.write(f"Описание: {note['content']}\n")
                file.write(f"Статус: {note['status']}\n")
                file.write(f"Дата создания: {note['created_date']}\n")
                file.write(f"Дедлайн: {note['issue_date']}\n")
                file.write("---" + "\n\n")  # Разделитель между заметками
    except PermissionError:
        print(f"Ошибка: у вас нет прав на запись в файл {filename}.")
    except Exception as e:
        print(f"Произошла ошибка при сохранении файла {filename}: {e}")

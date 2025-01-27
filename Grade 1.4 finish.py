import json
import yaml
import os
from collections import defaultdict


def save_notes_to_file(notes, filename):
    """Сохраняет заметки в JSON-файле."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Произошла ошибка при сохранении файла {filename}: {e}")


def load_notes_from_file(filename):
    """Загружает заметки из YAML-файла."""
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read().strip()

            if not content:
                return []

            notes = []
            current_note = defaultdict(str)
            lines = content.split("\n")

            for line in lines:
                if line.startswith("---"):
                    notes.append(dict(current_note))
                    current_note.clear()  # Очищаем текущий словарь для новой записи
                else:
                    key, value = line.split(":", 1)
                    current_note[key.strip()] = value.strip()

            if current_note:
                notes.append(dict(current_note))  # Добавляем последнюю запись

            return notes

        except Exception as e:
            print(f"Произошла ошибка при чтении файла {filename}: {e}")
        return

    with open(filename, 'w'):
        pass  # Создаем пустой файл
    print(f"Файл {filename} не найден. Создан новый файл.")
    return []


def handle_errors(filename):
    """Обрабатывает ошибки при работе с файлами."""
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass  # Создаем пустой файл
        print(f"Файл {filename} не найден. Создан новый файл.")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            if not content.strip():
                raise ValueError("Файл пуст.")
            # Дополнительная логика обработки данных...
    except (OSError, IOError) as e:
        print(f"Ошибка при доступе к файлу {filename}: {e}")
    except ValueError as e:
        print(f"Ошибка при обработке данных в файле {filename}: {e}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка при работе с файлом {filename}: {e}")


def append_notes_to_file(notes, filename):
    """Добавляет новые заметки в конец существующего файла."""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Произошла ошибка при добавлении заметок в файл {filename}: {e}")


def save_notes_yaml(notes, filename):
    """Сохраняет заметки в YAML-файле."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            yaml.safe_dump(notes, file, allow_unicode=True)
    except IOError as e:
        print(f"Произошла ошибка при сохранении файла {filename}: {e}")


if __name__ == "__main__":
    notes = [
        {
            "username": "Алексей",
            "title": "Список покупок",
            "content": "Купить продукты",
            "status": "новая",
            "created_date": "27-11-2024",
            "issue_date": "30-11-2024"
        }
    ]

    save_notes_to_file(notes, "notes.json")

    notes = load_notes_from_file("notes.yaml")
    print(notes)

    handle_errors("corrupted_file.txt")

    new_notes = [
        {
            "username": "Мария",
            "title": "План работы",
            "content": "Подготовить отчёт",
            "status": "в процессе",
            "created_date": "27-11-2024",
            "issue_date": "28-11-2024"
        }
    ]

    append_notes_to_file(new_notes, "notes.json")

    save_notes_yaml(notes, "notes.yaml")

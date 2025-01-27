import json


def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
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
        },
        {
            "username": "Иван",
            "title": "Отчет",
            "content": "Написать отчет по проекту",
            "status": "в процессе",
            "created_date": "28-11-2024",
            "issue_date": "29-11-2024"
        }
    ]

    save_notes_json(notes, "notes.json")

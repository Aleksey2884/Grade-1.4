import re


def load_notes_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        if not content.strip():
            return []

        notes = []
        current_note = {}
        lines = content.split("\n")

        for line in lines:
            if line.startswith("---"):
                notes.append(current_note)
                current_note = {}
            else:
                match = re.match(r'(.*?):\s*(.*)', line)
                if match:
                    key, value = match.groups()
                    current_note[key.strip()] = value.strip()

        # Добавляем последнюю заметку, так как она не завершается разделителем ---
        if current_note:
            notes.append(current_note)

        return notes

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return []


# Пример использования
if __name__ == "__main__":
    notes = load_notes_from_file("notes.txt")
    for note in notes:
        print(note)

import json
from pathlib import Path
from models import *


def students_to_json(students, path):

    json_file = Path(path)

    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат выходного файла: ожидается .json")

    if not isinstance(students, list):
        raise TypeError("students должно быть списком объектов Student.")

    for s in students:
        if not isinstance(s, Student):
            raise TypeError("Все элементы списка должны быть объектами Student.")

    data = [s.to_dict() for s in students]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):

    json_file = Path(path)

    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат входного файла: ожидается .json")

    if not json_file.exists():
        raise FileNotFoundError("Файл не найден")

    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Файл не является корректным JSON.")

    if not isinstance(data, list):
        raise TypeError("JSON должен содержать список студентов.")

    students = []
    for item in data:
        if not isinstance(item, dict):
            raise TypeError("каждый студент в JSON должен быть словарём.")
        students.append(Student.from_dict(item))

    return students

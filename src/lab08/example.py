from models import Student
from serialize import students_to_json, students_from_json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data', 'lab08')

os.makedirs(DATA_DIR, exist_ok=True)

# --- Создание объектов ---
s1 = Student("Линник Кристина Рустамовна", "2007-02-19", "БИВТ-25-06", 4.7)
s2 = Student("Иванов Петр Иванович", "2004-11-02", "БИВТ-22-02", 3.9)

print("Проверка age():", s1.age())
print("Проверка __str__():", s1)

students = [s1, s2]

# --- Сохранение в JSON ---
output_path = os.path.join(DATA_DIR, 'students_input.json')
students_to_json(students, output_path)

# --- Загрузка из JSON ---

input_path = os.path.join(DATA_DIR, 'students_input.json')
loaded_students = students_from_json(input_path)
print("Студенты, загруженные из JSON:")
for s in loaded_students:
    print(s, "| возраст:", s.age())

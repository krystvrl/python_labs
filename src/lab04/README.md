# **Лабораторная работа №4**
### **Задание №1**
```
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Читает содержимое текстового файла и возвращает его в виде строки.
    
    Аргументы:
        path (str | Path): Путь к файлу для чтения/строка
        encoding (str, optional): Кодировка файла. По умолчанию "utf-8".

    Для чтения файла в других кодировках укажите соответствующий параметр
    Пример:text = read_text("file.txt", encoding="cp1251")

    Поднимает:
    FileNotFoundError: Если файл не существует
    UnicodeDecodeError: Если указанная кодировка не соответствует 
    содержимому файла
    '''
    p = Path(path)
    print(p)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден")
    file_size = p.stat().st_size
    if file_size == 0:
        return ""
    try:
        return p.read_text(encoding=encoding)
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Ошибка кодировки: {e}")


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Создает/перезаписывает CSV файл с разделителем-запятой.
    
    Аргумент:
        rows: Итерируемый объект со строками данных (кортежи или списки)
        path: Путь к создаваемому CSV файлу
        header: Опциональный кортеж с названиями колонок для заголовка
    
    Поднимает:
        ValueError: Если строки в rows имеют разную длину
    """
    p = Path(path)
    rows_list = list(rows)
    if rows_list:
        row_length = len(rows_list[0])
        for row in rows_list:
            if len(row) != row_length:
                raise ValueError(f"Все строки должны иметь одинаковое количество элементов")
    
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for row in rows_list:
            writer.writerow(row)

```
![](images/lab04/io_txt_csv.jpg)

### **Задание №2**
```
import sys
from pathlib import Path
from io_txt_csv import read_text, write_csv
from text import *

def main():
    if len(sys.argv) < 2:
        print("Укажите путь к входному файлу")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = "../../data/lab04/report.csv"
    encoding = "utf-8" 
    if not output_file.lower().endswith(".csv"):
        raise ValueError(f"Неверный формат выходного файла: {output_file}. Ожидается .csv")
    
    try:
        text = read_text(input_file)
        if not text.strip():
            print("Входной файл пуст")
            write_csv([], output_file, header=('word', 'count'))
            return
        normalized = normalize(text)
        words = tokenize(normalized)
        freq = count_freq(words)
        top = top_n(freq, 5)
        topno = top_no(freq)
        total = len(words)
        unique = len(freq.items())
        write_csv(topno, output_file, header=('word', 'count'))
        print(f"Всего слов: {total}")
        print(f"Уникальных слов: {unique}")
        print("Топ-5:")
        for word, count in top:
            print(f"{word}:{count}")
        
    except FileNotFoundError:
        print(f"файл не найден")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```
![](images/lab04/consol.jpg)
![](images/lab04/report.csv.jpg)
![](images/lab04/report2.csv.jpg)

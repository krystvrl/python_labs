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

import sys
from pathlib import Path
from io_txt_csv import read_text, write_csv
from text import *


def main():
    if len(sys.argv) < 2:
        print("Укажите путь к входному файлу")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = "../../data/report.csv"
    encoding = "utf-8"
    if not output_file.lower().endswith(".csv"):
        raise ValueError(
            f"Неверный формат выходного файла: {output_file}. Ожидается .csv"
        )

    try:
        text = read_text(input_file)
        if not text.strip():
            print("Входной файл пуст")
            write_csv([], output_file, header=("word", "count"))
            return
        normalized = normalize(text)
        words = tokenize(normalized)
        freq = count_freq(words)
        top = top_n(freq, 5)
        topno = top_no(freq)
        total = len(words)
        unique = len(freq.items())
        write_csv(topno, output_file, header=("word", "count"))
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


if __name__ == "__main__":
    main()

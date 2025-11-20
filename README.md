# Лабораторная работа №6
### Пример 1. Подкоманды в одном CLI
``` python
import argparse
import os, sys
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.text import *

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command", required=True)  # Добавлен required=True

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()


    if args.command == "cat":
        file_path = Path(args.input)
        if not file_path.exists():
            parser.error(f"Файл '{args.input}' не найден")
            
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for i, line in enumerate(lines, 1):
                    if args.n:
                        print(f"{i:6d}\t{line.rstrip()}")
                    else:
                        print(line.rstrip())
        except FileNotFoundError:
            sys.exit(f"Ошибка: файл {args.input} не найден")
        except Exception as e:
            sys.exit(f"Ошибка: {e}")

    elif args.command == "stats":
        file_path = Path(args.input)
        if not file_path.exists():
            parser.error(f"Файл '{args.input}' не найден")
            
        try:
            with file_path.open("r", encoding="utf-8") as f:
                text = f.read()
            
            normalized = normalize(text)
            words = tokenize(normalized)
            freq = count_freq(words)
            top_words = top_n(freq, args.top)

            if not top_words:
                print("Слова не найдены в файле")
                return

            print(f"Топ {args.top} слов:")
            for word, count in top_words:
                print(f"{word}: {count}")
                
        except FileNotFoundError:
            sys.exit(f"Ошибка: файл {args.input} не найден")
        except Exception as e:
            sys.exit(f"Ошибка: {e}")

    else:
        # Если команда не указана, показываем справку
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
```
![cat](images/lab06/cat.jpg)
![stats](images/lab06/stats.jpg)

Меню помощи если не введена команда / --help
![help](images/lab06/help.jpg)


### Пример 2. CLI‑конвертер
``` python
import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command")

    parser1 = sub.add_parser("json2csv")
    parser1.add_argument("--in", dest="input", required=True)
    parser1.add_argument("--out", dest="output", required=True)

    parser2 = sub.add_parser("csv2json")
    parser2.add_argument("--in", dest="input", required=True)
    parser2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()
    if args.command == "json2csv":
        json_to_csv(args.input, args.output)    
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()
```
![csv](images/lab06/csv.jpg)
![json](images/lab06/json.jpg)
![xlsx](images/lab06/xlsx.jpg)

Меню помощи после введения подкоманды и --help
![subhelp](images/lab06/subhelp.jpg)

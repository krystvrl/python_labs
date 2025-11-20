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
#python -m src.lab06.cli_text cat --input data/samples/people.csv -n
#python -m src.lab06.cli_text stats --input data/samples/people.csv
#python -m src.lab06.cli_text --help

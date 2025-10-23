import sys
from collections import Counter

try:
    from lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
except ImportError:
    #Альтернативный импорт для тестирования
    import os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
from lib.text import normalize, tokenize, count_freq, top_n

def frequencies_from_text(text: str) -> dict[str, int]:
    """
    Генерация частот из текста .
    """
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """
    Сортировка частот по шаблону: (-частота, слово).
    """
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def generate_report():
    """
    Генерирует отчет по частотам слов.
    """
    input_file = "data/input.txt"
    output_file = "data/report.csv"
    
    try:
        # 1 Чтение текста 
        text = read_text(input_file)
        
        # 2 Подсчет частот через шаблонную функцию
        freq = frequencies_from_text(text)
        
        # 3 Сортировка по шаблону
        sorted_words = sorted_word_counts(freq)
        
        # 4 Сохранение отчета
        ensure_parent_dir(output_file)
        write_csv(sorted_words, output_file, header=("word", "count"))
        
        # 5 Вывод статистики в консоль
        tokens = tokenize(normalize(text))
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")
        print("Топ-5:")
        
        for word, count in top_n(freq, 5):
            print(f"{word}: {count}")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: Неверная кодировка файла {input_file}")
        print("Попробуйте указать кодировку: read_text(path, encoding='ваша кодировка')")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_report()
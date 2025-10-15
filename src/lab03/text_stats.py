#!/usr/bin/env python3
import sys
from lib.text import normalize, tokenize, count_freq, top_n


def main():
    """
    Читает текст из stdin, обрабатывает и выводит статистику.
    """
    # Читаем весь ввод до EOF
    text = sys.stdin.read().strip()
    
    if not text:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print("Топ-5:")
        return
    
    # Обрабатываем текст
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)
    
    # Выводим результаты
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
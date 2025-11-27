from text import *


def text_stats(n: str):
    n = input()
    norm = normalize(n)
    tokens = tokenize(norm)
    freq = count_freq(tokens)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-5:")
    top = top_n(freq)
    for key, value in top:
        print(f"{key}: {value}")


print(text_stats("Привет, мир! Привет!!!"))

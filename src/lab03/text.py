import re
import unicodedata


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст:
    - Приводит к casefold (лучше чем lower для Юникода)
    - Заменяет буквы ё/Ё на е/Е
    - Убирает невидимые управляющие символы, заменяя их на пробелы
    - Схлопывает повторяющиеся пробелы в один
    """
    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    # Заменяем управляющие символы и невидимые символы на пробелы
    text = "".join(
        char if char.isprintable() or char.isspace() else " " for char in text
    )

    # Схлопываем множественные пробелы в один
    text = re.sub(r"\s+", " ", text)

    # Убираем пробелы в начале и конце
    return text.strip()


def tokenize(text: str) -> list[str]:

    # Регулярное выражение для поиска слов (буквы/цифры/подчёркивание + дефис внутри)
    pattern = r"[\w]+(?:-[\w]+)*"
    tokens = re.findall(pattern, text)

    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитывает частоты токенов
    """
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает топ-N токенов по убыванию частоты
    При равенстве частот - по алфавиту
    """
    # Сортируем сначала по убыванию частоты, затем по возрастанию слова (алфавиту)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

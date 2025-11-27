def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    # if type(text) is not str:
    #     raise TypeError('Нужна строка')
    # import re
    # text = re.sub(r'\s+', ' ', text).strip()
    # if text=='':
    #     return ''
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = " ".join(text.strip().split())
    return text


def tokenize(text: str) -> list[str]:
    import re

    return re.findall(r"\w+(?:-\w+)*", text)
    # if type(text) is not str:
    #     raise TypeError('Нужна строка')
    # text=normalize(text)
    # # result=[]
    # token=[]
    # for character in text:
    #     if character.isalnum() or character=='_':
    #         token.append(character)
    #     elif character=='-' and token and token[-1].isalnum():
    #         token.append(character)
    #     else:
    #         if token and token[-1]!='-':
    #             result.append(''.join(token))
    #             token=[]
    # result.append(''.join(token))
    # return result


def count_freq(tokens: list[str]) -> dict[str, int]:
    if type(tokens) is not list:
        raise TypeError("Нужен список")
    return {word: tokens.count(word) for word in set(tokens)}


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if type(freq) is not dict:
        raise TypeError("Нужны словари")
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]


def top_no(freq: dict[str, int]) -> list[tuple[str, int]]:
    if type(freq) is not dict:
        raise TypeError("Нужны словари")
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))

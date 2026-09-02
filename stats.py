def word_counter(book: str, get_words_without_count: bool = False) -> int:
    words: list[str] = book.split()
    if get_words_without_count is False:
        return f"Found {len(words)} total words"
    return words


def character_count(text: str) -> dict[str, int]:
    characters = {}
    for char in text:
        characters[char.lower()] = characters.get(char.lower(), 0) + 1
    return characters


def sort_on(char: tuple[str, int]) -> int:
    return char[1]


def chars_dict_to_sorted_list(characters: dict[str, int]) -> list[tuple[str, int]]:
    characters_list: list = []
    for char, count in characters.items():
        characters_list.append((char, count))

    sorted_count = sorted(characters_list, reverse=True, key=sort_on)

    return sorted_count

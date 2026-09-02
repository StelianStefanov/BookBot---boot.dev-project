import sys

from stats import character_count, chars_dict_to_sorted_list, word_counter


def get_book_text(file_path) -> str:
    with open(file_path) as f:
        file_contents: str = f.read()

    return file_contents


def print_report(book, word_count) -> str:
    result = f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------"""

    result += f"\n{word_count}"
    result += "\n--------- Character Count -------"

    for char_and_count in chars_dict_to_sorted_list(character_count(book)):
        if char_and_count[0].isalpha():
            result += f"\n{char_and_count[0]}: {char_and_count[1]}"

    result += "\n============= END ==============="

    return result


def main() -> str:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book: str = get_book_text(sys.argv[1])

    return print_report(book, word_counter(book))


if __name__ == "__main__":
    print(main())

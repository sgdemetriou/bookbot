import sys
from stats import get_word_count, get_character_count, sort_dictionary


def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()
    return book_content


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    character_count = get_character_count(book_text)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print(f"--------- Character Count -------")
    for char in sort_dictionary(character_count):
        if not char['char'].isalpha():
            continue
        print(f"{char['char']}: {char['count']}")


main()
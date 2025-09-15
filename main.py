from stats import get_word_count, get_character_count


def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()
    return book_content


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    print(f"{word_count} words found in the document")
    print(character_count)


main()
def get_word_count(book_text):
    word_list = book_text.split()
    return len(word_list)


def get_character_count(book_text):
    character_count = {}
    for character in book_text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count
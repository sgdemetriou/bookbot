def get_word_count(book_text):
    word_list = book_text.split()
    return len(word_list)


def sort_on(items):
    return items["count"]


def sort_dictionary(character_count):
    char_list = []
    for char, count in character_count.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def get_character_count(book_text):
    character_count = {}
    for character in book_text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count
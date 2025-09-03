def get_num_words(str):
    num_words = len(str.split())

    return num_words


def get_char_count(str):
    char_count = {}

    formatted_str = str.lower()

    for c in formatted_str:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

    return char_count

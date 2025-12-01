def get_num_words(str):
    words = str.split()
    num_words = len(words)

    return num_words

def get_chars(str):
    chars = {}
    sanitized = str.lower()

    for c in sanitized:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return chars

def get_char_list(dct):
    char_list = []
    for c in dct.items():
        char_list.append({"char": c[0], "num": c[1]})

    char_list.sort(reverse = True, key = sort_on)

    return char_list

def sort_on(items):
    return items["num"]

import sys
from stats import get_num_words, get_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def sort_on(items):
    return items[1]


def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_char = get_char_count(text)

    char_list = list(num_char.items())

    char_list.sort(reverse=True, key=sort_on)

    for c in char_list:
        if c[0].isalpha():
            print(f"{c[0]}: {c[1]}")

    print("============= END ===============")


main()

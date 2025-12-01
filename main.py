import sys
from stats import get_num_words, get_chars, get_char_list

def get_book_text(filepath):
    # the with block closes the file when the block is exited, cleaning up ressources.
    with open(filepath) as f:
        content = f.read()
    return content

def make_report(path, num, list):
    report = f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num} total words
--------- Character Count -------
"""
    for l in list:
        if l["char"].isalpha():
            report += f"{l["char"]}: {l["num"]}\n"

    report += "============= END ==============="

    return report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("path", path)

    string_content = get_book_text(path)
    num_words = get_num_words(string_content)
    char_count = get_chars(string_content)
    print(f"Found {num_words} total words")
    char_list = get_char_list(char_count)
    report = make_report(path, num_words, char_list)
    print(report)

main()

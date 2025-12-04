import sys
from stats import count_words, count_char, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def main():
    try:
        filepath = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(filepath)
    total_words = count_words(book_text)
    dict_values = count_char(book_text)
    sorted_dict = sort_dict(dict_values)
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {filepath}...")
    print("-" * 12 + " Word Count " + "-" * 12)
    print(f"Found {total_words} total words")
    print("-" * 12 + " Characther Count " + "-" * 12)
    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")
    print("=" * 12 + " END " + "=" * 12)

main()

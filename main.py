def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print(book_text)

main()

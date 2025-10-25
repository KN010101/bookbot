from stats import get_num_words, get_char_count

def main():
    book_path = "/home/kadmin/workspace/github.com/KN010101/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print(f"{num_words} words found in the document")
    for char, count in char_count.items():
        print(f"'{char}': {count}")


def get_book_text(path):
    """
    Reads the content of a text file.

    Parameters:
        path (str): The path to the text file.

    Returns:
        str: The content of the file as a string.
    """
    with open(path) as f:
        return f.read()

main()

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_word_count(string):
    return len(string.split())

def main():
    num_words = get_word_count(get_book_text("./books/frankenstein.txt"))
    print(f"Found {num_words} total words")

main()

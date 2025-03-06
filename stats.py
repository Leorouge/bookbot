def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

get_num_words()

def get_book_text():
    with open(books/frankenstein.txt) as f:
        file_contents = f.read()

def main():
    call get_book_text
    print (file_contents)

main()



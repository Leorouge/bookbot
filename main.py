import sys
from stats import get_book_text, count_words, character_count, sort_characters

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    char_dict = character_count(text)
    sorted_chars = sort_characters(char_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_info in sorted_chars:
        print(f"{char_info['char']}: {char_info['count']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()
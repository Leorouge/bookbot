def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def get_num_words():
    text = get_book_text(path)
    num_words = count_words(text)

def character_count(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in characters:
                characters[lowered] += 1
            else:
                characters[lowered] = 1
    return characters

def sort_characters(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=lambda x: x["count"])
    return chars_list


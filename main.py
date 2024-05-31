def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path) 
    num_words = word_count(text) 
    characters_dict = get_charact_dict(text)
    characters_sorted_list = charact_dict_to_sorted_list(characters_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in this document")


    for item in characters_sorted_list:
        character = item["character"]
        count = item["num"]
        print(f"The '{character}' character was found {count} times")

    print(f"--- End report ---")


def word_count(text):
    words = text.split()
    return len(words)


def sort_on(x):
    return x["num"]


def charact_dict_to_sorted_list(characters_dict):
    sorted_list = []
    for ch in characters_dict:
        sorted_list.append({"character": ch, "num": characters_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_charact_dict(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in characters:
                characters[lowered] += 1
            else:
                characters[lowered] = 1
    return characters


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
























































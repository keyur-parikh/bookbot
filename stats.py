def num_of_words(text: str) -> int:
    # Takes a text, split the words, and return the length of the list
    list_of_words = text.split()
    return len(list_of_words)

def count_characters(text:str) -> dict:
    character_count = {}
    for letter in text:
        letter = letter.lower()
        if letter not in character_count:
            character_count[letter] = 1
        else:
            character_count[letter] += 1
    return character_count

def sort_character(character_count: dict) -> list:
    sorted_characters = sorted(character_count.items(), key = lambda x: x[1], reverse=True)
    output = []
    for pair in sorted_characters:
        key_value = {pair[0]: pair[1]}
        output.append(key_value)


    return output

from stats import num_of_words, count_characters, sort_character
import sys

def get_book_text(filepath: str) -> str:
    # Opens the file and reads the contents and returns it as a string
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    no_of_words = num_of_words(text)

   # print(f"{no_of_words} words found in the document")
    unsorted_character = count_characters(text)
    character_count = sort_character(unsorted_character)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {no_of_words} total words")
    print("--------- Character Count -------")
    for element in character_count:
       for key, value in element.items():
           if key.isalpha():
                print(f"{key}: {value}")
    print("============= END ===============")
main()
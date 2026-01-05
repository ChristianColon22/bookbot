from stats import get_num_words, count_characters, sort_character_dict
import sys


def get_book_text(path_to_file):
    try: 
        with open(path_to_file) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"File not found at specified path: {path_to_file}")
        sys.exit(1)



def generate_report(path):
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("----------- Word Count ----------")
    for entry in sort_character_dict(count_characters(text)):
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    generate_report(sys.argv[1])

main()

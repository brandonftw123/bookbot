from stats import get_num_words, count_characters, sorted_characters
import sys

# Returns file in string format
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        book_string = get_book_text(book_path)
        num_words = get_num_words(book_string)
        char_dict = count_characters(book_string.lower())
        sorted_char_dict = sorted_characters(char_dict)

    # Formatted output
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_char_dict:
            if item["character"].isalpha():
                print(f"{item["character"]}: {item["count"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
main()
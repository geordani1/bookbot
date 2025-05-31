import sys
from collections import Counter
from stats import get_word_count

def number_characters(text):
    char_counts = Counter(text.lower())  # Convert to lowercase for case-insensitive counting
    for char, count in sorted(char_counts.items()):
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        with open(book_path, 'r', encoding='utf-8') as f:
            book_text = f.read()
    except FileNotFoundError:
        print(f"Error: file '{book_path}' not found.")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    number_characters(book_text)
    print("============= END ===============")

if __name__ == '__main__':
    main()

def get_word_count(text):
    words = text.split()
    return len(words)

def number_characters(text_content):
    char_count = {}

    for char in text_content:
        char = char.lower()
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

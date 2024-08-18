import sys
import re

def clean_text(input_text):
    words_to_remove = ['fucking', 'fuck off', 'fuck']

    for word in words_to_remove:
        pattern = r'\b' + re.escape(word) + r'\b\s*'
        input_text = re.sub(pattern, '', input_text)

    return input_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python text_cleaner.py --file <file_path> or --text '<input_text>'")
    else:
        if sys.argv[1] == '--file' and len(sys.argv) == 3:
            file_path = sys.argv[2]
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                cleaned_text = clean_text(text)
                print("Cleaned Text:")
                print(cleaned_text)
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' does not exist.")
        elif sys.argv[1] == '--text' and len(sys.argv) == 3:
            text = sys.argv[2]
            cleaned_text = clean_text(text)
            print("Cleaned Text:")
            print(cleaned_text)
        else:
            print("Invalid input. Usage: python text_cleaner.py --file <file_path> or --text '<input_text>'")

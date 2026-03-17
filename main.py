from stats import number_of_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
	path = "books/frankenstein.txt"
	text = get_book_text(path)
	count = number_of_words(text)
	print(f"Found {count} total words")

main()

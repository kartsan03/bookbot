from stats import number_of_words, number_of_letters, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
	print("============ BOOKBOT ============")
	path = "books/frankenstein.txt"
	print(f"Analyzing book found at {path}")
	text = get_book_text(path)
	count = number_of_words(text)
	print("----------- Word Count ----------")
	print(f"Found {count} total words")
	print("--------- Character Count -------")
	for item in sorted_list(number_of_letters(text)):
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

main()

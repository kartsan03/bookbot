def number_of_words(text):
        number = len(text.split())
        return number

def number_of_letters(text):
	lowered_text = text.lower()
	new_dict = {}
	for char in lowered_text :
		if char in new_dict :
			new_dict[char] += 1
		else :
			new_dict[char] = 1
	return new_dict

def sort_on(items):
	return items["num"]

def sorted_list(text):
	finished_dictionary = []
	for pair in text:
		finished_dictionary.append({"char": pair, "num": text[pair]})
	finished_dictionary.sort(key=sort_on, reverse=True)
	return finished_dictionary

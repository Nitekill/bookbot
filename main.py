from collections import Counter

def count_letters(book):
	freq = Counter(book.lower())
	freq = {key: value for key, value in freq.items() if key.isalpha()}
	return freq

def count_words(book):
	number_of_words = 0
	lines = book.split()
	number_of_words += len(lines)
	return number_of_words


def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		#print(file_contents)
		print("--- Begin report of books/frankenstein.txt ---")
		print(f"{count_words(file_contents)} words found in the document")
		freq_counter = count_letters(file_contents)
		for key, value in freq_counter.items():
			print(f"The '{key}' was found in the document {value} times")
		



main()

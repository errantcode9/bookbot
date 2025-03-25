from stats import count_words, count_chars, chars_dict_to_sorted_list
from sys import argv, exit

 

if len(argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
    # Give console error if invoked with no file path
else:
    book_path = argv[1]
    # Define book path as second string in argv

def main(book_path):
    
    # Read the contents of the file
    with open(book_path) as f:
        contents = f.read()
    
    # Count the words using your function
    word_count = count_words(book_path)
    
    # Count the characters
    char_counts = count_chars(contents)
    
    # Get the sorted list of character counts
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    # Now print the report according to the specified format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count, but only if it's alphabetical
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

# Call the main function
if __name__ == "__main__":
    main(book_path)
def count_words(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
        results = contents.split()
        return len(results)


def count_chars(text):
    char_counts = {}
    for char in text.lower():
        # Increment the count for this character
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


def chars_dict_to_sorted_list(char_counts):
    # Create a list to hold our dictionaries
    chars_list = []
    
    # For each character and its count in the dictionary
    for char, count in char_counts.items():
        # Create a dictionary with "char" and "count" keys
        char_dict = {"char": char, "count": count}
        # Add it to our list
        chars_list.append(char_dict)
    
    # Define the function to tell sort() which value to use
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list by count in descending order
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list


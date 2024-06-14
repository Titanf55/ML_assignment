import string

def remove_punctuation(input_string):
    # Define punctuation characters
    punctuation_chars = string.punctuation

    # Create a translation table to map each punctuation character to None
    translation_table = str.maketrans("", "", punctuation_chars)
#str.maketrans(x, y, z) returns a translation table that maps each character in string x to 
# the character at the same position in string y. 
# Optionally, it also removes characters specified in string z.
#here we are coverting none to none but removing punctuations.

    # Remove punctuation using translate method
    clean_string = input_string.translate(translation_table)
#translate(table) method returns a copy of the string
#where each character has been mapped through the given translation table.

    return clean_string

# Example usage:
input_string = "Hello! How are you doing? I'm doing fine, thank you."
cleaned_string = remove_punctuation(input_string)
print("Original string:", input_string)
print("String without punctuation:", cleaned_string)

import string

def is_pangram(input_str):
    input_str = input_str.lower()
    alphabet_set = set(string.ascii_lowercase)
    input_str_set = set(input_str)
    return alphabet_set.issubset(input_str_set)

input_str = input("Enter a string: ")

if is_pangram(input_str):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")


    
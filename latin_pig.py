"""Writing code for the latin pig challenge."""
def main():
    """Take input from the user and calls latin pig."""
    print("Welcome to latin pig\n\n")
    print("Enter a word and get a latin pig\n\n")
    user_input = input("Enter a word:")
    latin_pig(user_input)

def latin_pig(string):
    """Convert the input into a pig latin."""
    first_char = string[0].tolower()
    rest_string = string[1:]
    if (first_char == 'a' or first_char == 'e' or first_char == 'i' or
            first_char == 'o' or first_char == 'u'):
        string_latin_pig = string + "way"
        print_latin_pig(string_latin_pig)
    else:
        string_latin_pig = rest_string + first_char + "ay"
        print_latin_pig(string_latin_pig)

def print_latin_pig(string):
    """Print the output converted pig latin."""
    print("\nYour latin pig or pig latin is:\n\n")
    print(string)







if __name__ == "__main__":
    main()

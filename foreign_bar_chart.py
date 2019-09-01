"""Map letters from string into dict & print a bar chart."""
import sys
import pprint

def main():
    """input the text and create the bar chart."""
    english_text = input("Enter an english test: ")
    spanish_text = input("Enter the spanish translation of the above text: ")

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabets_key = list(alphabets)
    english_dict = {key:[] for key in alphabets_key}
    spanish_dict = {key:[] for key in alphabets_key}
    for char in english_text:
        char = char.lower()
        if char in alphabets:
            english_dict[char].append(char)

    for char in spanish_text:
        char = char.lower()
        if char in alphabets:
            spanish_dict[char].append(char)

    print("\nEnglish text = ", end='')
    print("{}\n".format(english_text), file=sys.stderr)
    print("\n Bar Chart of English text:\n")
    pprint.pprint(english_dict, width=110)

    print("\nSpanish text = ", end='')
    print("{}\n".format(spanish_text), file=sys.stderr)
    print("\n Bar Chart of Spanish text:\n")
    pprint.pprint(spanish_dict, width=110)

if __name__ == "__main__":
    main()

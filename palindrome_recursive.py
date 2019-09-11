"""Program to check the palidrome using recursive."""
import sys

def loaddictionary(dictionaryname):
    """Load the dictionary into a list."""
    try:
        with open(dictionaryname) as in_file:
            word_in_list = in_file.read().strip().split('\n')
            word_in_list = [x.lower() for x in word_in_list]
            return word_in_list
    except IOError as error:
        print("{}\nError opening {}.Terminating!".format(error, dictionaryname), file=sys.stderr)
    sys.exit(1)

def palindrome(word):
    """Check the palindrome and return true or false."""
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
    return False

def main():
    """Append the palindromes in the file."""
    filename = input("Enter the name of the dictionary file: ")
    word_list = loaddictionary(filename)
    pali_list = []
    for word in word_list:
        if len(word) > 1:
            is_palindrome = palindrome(word)
            if is_palindrome:
                pali_list.append(word)
    print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
    print(*pali_list, sep='\n')

if __name__ == "__main__":
    main()

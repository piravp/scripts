import itertools

words = []


# Replace wordlist.txt with words/numbers/special-characters.
# Seperate with a new line.
def readfile():
    with open("wordlist.txt", "r") as file:
        global words
        words = file.read().lower().split()
        print("Words read from file: ", words)
        print()


def bruteforce_passwd(word_casing=False, letter_by_letter=False, number_of_words=None):
    n = 0

    # Create permutations using words from file, specify how many words to create combo from (default=all)
    word_combinations = itertools.permutations(words, number_of_words)

    # Generate passwords with various combinations of capitalized words (more combinations)
    if word_casing:
        for word in word_combinations:
            print("Now considering sequence:", word)

            # Uppercase letter by letter (warning! this creates really much output)
            if letter_by_letter:
                word = ''.join(word)
            letter_combination = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in word)))

            for letter in letter_combination:
                n += 1
                print(letter)
        print(n, "permutations.")
        return

    # Consider password as all lower case (fewer combinations)
    for word in word_combinations:
        n += 1
        print(''.join(word))
    print(n, "permutations.")

#TODO: Don't capitalize specialcharacters/numbers

def main():
    readfile()
    print("Bruteforcing...")
    # Set number_of_words=None to use all words in wordlist.txt
    bruteforce_passwd(word_casing=True, letter_by_letter=True, number_of_words=None)


if __name__ == "__main__":
    main()
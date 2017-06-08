# Password bruteforcer

Pretty self explanatory, no?

Generates a wordlist with different combinations which can be used for a bruteforce attack.

## Usage
Add any string to [wordlist.txt](wordlist.txt) - separate with a new line.

Look for this function inside the ```main```-method:
```python
bruteforce_passwd(word_casing=True, letter_by_letter=False, number_of_words=None)
```

* *word_casing*
    * When true, the script will make combinations of both lower- and upper-case words.

* *letter_by_letter*
    * When true, the script will create a different combination for every single letter.
    This will only work if ```word_casing``` is set to true.

* *number_of_word*
    * Will take the first x number of words and permutate. To consider every given word in the
    .txt file set the variable to ```None```.



## To-Do
- [ ] Refactoring
- [ ] Write results to file (Optional)

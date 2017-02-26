import re
import argparse





FILENAME = "commentfile.py"


def block():
    block_comments = 0
    with open(FILENAME, "r") as file:

        # check for block comments
        for line in file:

            reg = re.search("^\s*#",line)
            # if not none
            if reg:
                block_comments += 1
                #print(line)

    return block_comments


def multi():

    # multi-line comments
    fileAsString = open(FILENAME).read()

    # M-flag: Match over multiple lines
    # S-flag: Makes . match any character including newline
    regex_flags = re.M | re.S

    match = re.findall("^\"\"\".*?\"\"\"", fileAsString, regex_flags)
    multiline_comments = len(match)
    #print("Multi-line comments:", multiline_comments)

    return multiline_comments

def main():
    singleC = block()
    multiC = multi()
    print("--")
    print("Single comments found:", singleC)
    print("Multi comments found:", multiC)
    print("Total comments found:", singleC+multiC)





if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="This is code comment counter for Python.",add_help="Comment code counter for python.")
    # parser.print_help()
    main()
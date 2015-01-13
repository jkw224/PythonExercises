

def count_characters():
    # Take random string as input
    # Produce a dictionary of characters mapped to integer frequencies
    pass

def print():
    # Pretty-print a dictionary
    pass                             # string.split
                                     # with opens file
with open("myfile.txt", r) in file:  # file is iteratable (line is literally the str we wrote to the file
    # Count characters in the string
    counts = count_characters(random_string)
    print_output(counts)

#
#
# .upper
# .lower
#

#################
### string.split
#################

# ~~~~~~~~~~~~~
import string

def remove_single_quotes(s):
    # Remove single quotes form s if those single quotes occeur at the beginnning or end of the string.

    if s[0] == "'":  # removes first single quote
        s = s[1:]

    if s[-1] == "'":  # removes last single quote
        s = s[:-2]

my_string = 'Here\'s a "sentence" from the book that I\'m reading.'

my_words = my_string.split('e')  # splits on e
my_words = my_string.split()  # splits on white space

print(my_words)


# ~~~~~~~~~~~~~~
for word in my_words:
    parsed_word = word.translate(None, "") # removes single string
    parsed_word_punct = word.translate(None, string.punctuation) # removes punctuation
    parsed word_sing_quotes = word.translate(None, string.punctuation)
    print(word)

#
#
#
#
#############################
### generating random string
#############################

import random
import string
from random import randint


def random_string_loop():
    with open("exercises_five.dat", "r+") as f:

    for num in range(0, 10):  # Represents number of strings printed

        random_integer = randint(0, 101)
        random_string = ''.join([random.choice(string.ascii_letters) for i in range(0, random_integer)])  # Represents number
        # of char within string
        # with open("exercise_five.dat", "r+") as f:
        #     f.write(random_string)

        print(random_string)
        print(len(random_string))

        f.write(random_string + "\n")


# Questions:
# ~~~~~~~~~~
# Importing modules
# .format()

l = [1, 2, 3, 4]

for num in l:
    print("Hello")
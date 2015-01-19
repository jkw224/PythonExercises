import string
from random import randint, SystemRandom


# Creates random-length string of random characters (upper, lower, digits)
def random_string_gen(num):
    with open("exercise_five.dat", "w+") as five_file:

        # print("\n*****  File contents  ******\n")
        for i in range(num):
            characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
            n = randint(0, 100)
            for x in range(n):
                concatted_string = ''.join(SystemRandom().choice(characters) for _ in range(n))

            five_file.write(concatted_string + '\n')
            # print(str(i) + " " + concatted_string)
            # print("%d %s" % (i, concatted_string))


# Prints number of occurrences of each character
def character_count():
    with open("exercise_five.dat", "r") as ex5:
        test_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        ex5_contents = ex5.read()

        for i in range(len(test_characters)):
            occurrence_count = 0
            if test_characters[i] ==
                occurrence_count += 1
                print("%s ==> %d" % (test_characters[i], occurrence_count))


# Josh Hancock's version:
def counter(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
        dictionary = {}
        for character in contents:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
    return dictionary



##############
## Start Here
##############

how_many_strings = input("How many random strings do you want printed out?")

while True:
    try:
        int(how_many_strings)
    except ValueError:
        how_many_strings = input("Please enter a number: ")
        continue
    else:
        break

random_string_gen(int(how_many_strings))
print("\nFile is now written. Counting characters...\n")
character_count()



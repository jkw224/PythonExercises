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
            # print(str(i) + " " + concatted_string)
            # print("%d %s" % (i, concatted_string))
            five_file.write(concatted_string + '\n')

def string_count():
    with open("exercise_five.dat", "r") as ex5:
    test_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    for i in range(len(test_characters)):
        occurance_count = 0
        if test_characters[i] ==
            occurance_count += 1
            print("%s ==> %d" % (test_characters[i], occurance_count))

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



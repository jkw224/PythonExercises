# from string import ascii_letters, digits
# from random import choice
# from random import randint
#
#
# def print_header():
#     for i in range(0, 10):
#         random_integer = randint(0, 101)
#     star_divider = "* " * 15
#     which_random_string = str(i + 1)
#     num_of_chars = str(random_integer)
#     print("\n %s Random String %s has %s characters %s" % (star_divider, which_random_string, num_of_chars, star_divider))
#
#
# def random_string_gen():
#     s = []
#     glue = ", \n"
#     for j in range(0, random_integer):
#         my_char = choice(ascii_letters, digits)  # string.choice selects a random characters (from random_integer)
#         s.append(my_char)
#     print("\n %s \n" % (glue.join(s)))
#     with open("exercise_five.dat", "w") as five:
#         five.write(s)
#
with open("exercise_five.dat", "r+") as f:
    content = f.read()
    d = dict()
    for character in content:
        d[character] = d.get(character, 0) + 1
        print((str(character) + " => " + str(d[character]))),
        # print(" " * 3)


# Josh's code
# def counter():
#     with open("exercise_five.dat", 'r') as f:
#         contents = f.read()
#         dictionary = {}
#         for character in contents:
#             if character in dictionary:
#                 dictionary[character] += 1
#             else:
#                 dictionary[character] = 1
#     return dictionary
#
# print(counter())
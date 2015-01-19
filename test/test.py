# from string import ascii_letters, digits
# from random import choice, randint
#
#
# def random_string_gen():
#     for i in range(0, 10):
#         random_integer = randint(0, 101)
#
#         s = []
#         glue = ", \n"
#         for j in range(0, random_integer):
#             char_set = ascii_letters, digits
#             my_char = choice(char_set)# string.choice selects a random characters (from random_integer)
#             s.append(my_char)
#         print("\n %s \n" % (glue.join(s)))
#
# print(random_string_gen())


with open("exercise_five.dat", "a+") as f:
    content = f.read()

print(type(content))
print(str(content))

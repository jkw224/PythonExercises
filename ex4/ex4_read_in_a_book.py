import string
from random import choice
from random import randint

for i in range(0, 11):
    random_string = generate_random_string()
    return random_string


def generate_random_string():
    random_integer = randint(0, 101)
    s = ''

    for i in range (0, random_integer):
        my_char = choice(string.letters)
        s += my_char

    print(s)


# my_char = choice(string.letters)
#
# print my_char
# print randint(0, 101)




#######################
# General Syntax
#######################

if i in my_dict:
    my_dict[i] += 1
else:
    my_dict[i] = 1



################################
# Two Version of Same Thing...
################################

for word in file:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#####
# vs
#####

for c in a_string:
    d[c] = d.get(c, 0) + 1

print(c)

# d = dict(a=0, b=0, c=0)  //Dictionary constructor
d = {                    # //Dictionary literal
    "a": 0,
    "b": 0,
    "c": 0
}

d["a"] += 1
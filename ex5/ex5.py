import string
from random import randint, SystemRandom


def random_string_gen():
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    n = randint(0, 100)
    concatted_string = ''.join(SystemRandom().choice(characters) for _ in range(n))
    return concatted_string


def write_ten_random_strings():
    with open("exercise_five.dat", "w") as file:
        for i in range(10):
            n = random_string_gen()
            file.write(n + '\n')


def character_count():
    with open("exercise_five.dat", "r+") as file:
        content = file.read()
        d = dict()
        for character in content:
            d[character] = d.get(character, 0) + 1
            print((str(character) + " => " + str(d[character]))),


write_ten_random_strings()
character_count()




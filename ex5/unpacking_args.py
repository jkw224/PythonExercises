# Unpacking arguments (*args, **kwargs)
# -------------------------------------


def print_three_things(a, b, c):
    print('a = {0}, b = {1}, c = {2'.format(a, b, c))

my_list = ['aardvark', 'baboon', 'cat']

print(*my_list)


my_map = [[],[],[]]
def replace_pixel(replacement_character, original_character, x, y):

    if x == -1 or y == -1:  #
        return

    if x >= len(my_map[0]):  # horizontal check
        return

    if y >= len(my_map):  # vertical check
        return

    if my_map[x][y] = original_character:  # list of lists
        my_map[x][y] = replacement_character

    replace_pixel(replacement_character, original_character, x-1, y)
    replace_pixel(replacement_character, original_character, x+1, y)
    replace_pixel(replacement_character, original_character, x, y-1)
    replace_pixel(replacement_character, original_character, x, y+1)


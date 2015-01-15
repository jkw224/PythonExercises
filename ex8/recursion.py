def sum_list(l, n=0):
    if n >= len(l):
        return 0

    current_value = l[n]
    n += 1
    current_value += sum_list(l, n)
    return current_value

print(sum_list([1, 2, 3, 4, 5]))



def recursive_pop_sum(list):
    if not list:
        return 1

    list =- 1
    recursive_pop_sum()



print(recursive_pop_sum(my_list([1, 2, 3, 4, 5])))
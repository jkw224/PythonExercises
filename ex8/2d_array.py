l = []

with open("map.txt", "r") as f:
    for line in f:
        l.append([])
        for character in line:
            if character != '\n':
                l[-1].append(character)


# l[7][11] = "A"

print(l[7])
print(l[7][11])

for row in l:
    print(row)
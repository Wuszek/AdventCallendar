with open('list.txt') as f:
    lines = [int(line) for line in f.readlines()]

def prize(L):
    pair_list = []
    C = 2020

    for x in L:
        for y in L:
            for z in L:
                # if x != y | To prevent 1 + 1 and 2 + 2 (following example)
<<<<<<< HEAD
                # (y, x) not in pair_list | Prevent inverted pairs
                if x != y and x != z and z != y and x + y + z== C and (y, x, z) not in pair_list:
=======
                # (y, x, z) not in pair_list | Prevent inverted triples
                if x != y and x != z and y != z and x + y + z == C and (y, x, z) not in pair_list \
                        and (z, y, x) not in pair_list and (z, x, y) not in pair_list and (y, z, x) not in pair_list\
                        and (x, z, y) not in pair_list:
>>>>>>> c0ba25a... Day2 part2 excercise
                    pair_list.append((x, y, z))
                    multiplied = x*y*z

    return pair_list, multiplied

print (prize(lines))



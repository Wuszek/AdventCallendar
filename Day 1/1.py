with open('list.txt') as f:
    lines = [int(line) for line in f.readlines()]

def prize(L):
    pair_list = []
    C = 2020

    for x in L:
        for y in L:
            for z in L:
                # if x != y | To prevent 1 + 1 and 2 + 2 (following example)
                # (y, x) not in pair_list | Prevent inverted pairs
                if x != y and x != z and z != y and x + y + z== C and (y, x, z) not in pair_list:
                    pair_list.append((x, y, z))
                    multiplied = x*y*z

    return pair_list, multiplied

print (prize(lines))




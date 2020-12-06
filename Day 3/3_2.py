with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

trees_count = []


def tree_counter(L, r, d):
    n = 0
    m = 0
    tree_count = 0

    for x in L:
        set_point = list_input[n][m]
        # print("n:", n, "m:", m)
        # print(set_point)
        # print(list_input[n])
        n += d  # 1 down
        m += r  # 3 right

        if m >= 31:
            m = m - 31

        if n > 323:
            break

        if set_point == "#":
            tree_count += 1

    trees_count.append(tree_count)


tree_counter(list_input, 1, 1)
tree_counter(list_input, 3, 1)
tree_counter(list_input, 5, 1)
tree_counter(list_input, 7, 1)
tree_counter(list_input, 1, 2)

print("List of results:", trees_count)

result = 1
for x in trees_count:
    result = result * int(x)

print("Multiplied:", result)




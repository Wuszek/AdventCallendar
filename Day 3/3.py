with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

def tree_counter(L):

    n = 0
    m = 0
    tree_count = 0

    for x in L:
      set_point = list_input[n][m]
      print("n:", n, "m:", m)
      print(set_point)
      print(list_input[n])
      n += 1
      m += 3

      if m >= 31:
          m = m - 31

      if set_point == "#":
          tree_count += 1

    print(tree_count)

tree_counter(list_input)
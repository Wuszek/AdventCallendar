with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

def correct_pass_count(L):

    line = 0
    correct_pass_number = 0

    for x in L:
        split = list_input[line].split(' ')

        limit_split = split[0].split('-')
        position1 = limit_split[0]
        position2 = limit_split[1]
        selected_character = split[1][0]

        line += 1

        # print("Selected char:", selected_character)
        # print(split[2][int(position1) - 1], "from position", position1)
        # print(split[2][int(position2) - 1], "from position", position2)

        if split[2][int(position1)-1] == selected_character and split[2][int(position2)-1] == selected_character:
            print("Same characters on both positions. Password NOT OK")
        elif split[2][int(position1)-1] == selected_character or split[2][int(position2)-1] == selected_character:
            print("Correct password")
            correct_pass_number += 1
        else:
            print("No selected character. Password NOT OK")

    print("Number of correct passwords is:", correct_pass_number)

correct_pass_count(list_input)




with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

def correct_pass_count(L):

    line = 0
    correct_pass_number = 0

    for x in L:
        count = 0
        split = list_input[line].split(' ')

        limit_split = split[0].split('-')
        lower_limit = limit_split[0]
        upper_limit = limit_split[1]
        selected_character = split[1][0]

        line += 1
        for i in split[2]:
            if i == selected_character:
                count += 1
        # print("Liczba znakow: " , count)
        # print("Gorny limit: " , int(upper_limit))
        # print("Dolny limit: " , int(lower_limit))

        if int(lower_limit) <= count <= int(upper_limit):
            correct_pass_number += 1
        #     print('Password OK')
        # else:
        #     print('Password NOT OK')

    print(correct_pass_number)

correct_pass_count(list_input)




with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

def answer_counter(L):

    sum_string = ""
    counts_sum = 0
    for x in L:

        if x != "":
            sum_string = sum_string + x
        else:
           unique = len(set(sum_string))
           sum_string = ""
           counts_sum += unique

    print(counts_sum)

answer_counter(list_input)
with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

#print(list_input)

def answer_counter(L):

    n = 0
    sum_string = ""
    counts_sum = 0
    for x in L:
        temp_string = list_input[n]
        #print(temp_string)

        if temp_string != "":
            sum_string = sum_string + temp_string
            #print(sum_string)
            n += 1

        else:
           unique = len(set(sum_string))
           #print(unique)
           sum_string = ""
           n += 1
           counts_sum += unique

    print(counts_sum)

answer_counter(list_input)
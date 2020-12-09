from collections import Counter

with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

def answer_counter(L):

    freq = {}
    sum_string = ""
    counts_sum = 0
    people_count = 0
    for x in L:

        if x != "":
            sum_string = sum_string + x
            people_count += 1

        elif x =="":
            for keys in sum_string:
                freq[keys] = freq.get(keys, 0) + 1

            for x in freq:
                if freq.get(x, 0) == people_count:
                    counts_sum += 1

            freq = {}
            sum_string = ""
            people_count = 0

    print("Suma:" + str(counts_sum))

answer_counter(list_input)
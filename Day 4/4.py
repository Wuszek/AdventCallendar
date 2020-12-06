with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

print(list_input)


def passport_checker(L):

    n = 0
    m = 0
    passport_rate = 0
    key_counter = 0

    for x in L:
        search_string = list_input[n]

        print(search_string)
        if list_input[n] != "":
            if "ecl" in search_string:
                key_counter += 1
            if "pid" in search_string:
                key_counter += 1
            if "eyr" in search_string:
                key_counter += 1
            if "hcl" in search_string:
                key_counter += 1
            if "byr" in search_string:
                key_counter += 1
            if "iyr" in search_string:
                key_counter += 1
            if "hgt" in search_string:
                key_counter += 1
        else:
            if key_counter >= 7:
                print("PASSPORT VALID")
                passport_rate += 1
                print("Passport count:", passport_rate)
                print("\r")

            else:
                print("PASSPORT INVALID")
                passport_rate = passport_rate

            key_counter = 0
            m += 1
        n += 1


passport_checker(list_input)
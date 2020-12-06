import re
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
            if "byr" in search_string:
                index = search_string.index("byr")
                birthday_date = search_string[index+4:]
                birthday_date2 = search_string[index+4:index+8]

                numeric = 0
                for i in birthday_date:
                    if i.isdigit():
                       numeric += 1
                       #print(numeric)
                    else:
                        break
                if numeric == 4:
                    if 1920 <= int(birthday_date2) <= 2002:
                        key_counter += 1

                else:
                    print("Wrong birthday date (1920-2002)")

            if "iyr" in search_string:
                index = search_string.index("iyr")
                issue_date = search_string[index+4:]
                issue_date2 = search_string[index+4:index+8]
                numeric = 0
                for i in issue_date:
                    if i.isdigit():
                        numeric += 1
                        #print(numeric)
                    else:
                        break
                if numeric == 4:
                    if 2010 <= int(issue_date2) <= 2020:
                        key_counter += 1

                else:
                    print("Wrong issue year (2010-2020)")

            if "eyr" in search_string:
                index = search_string.index("eyr")
                exp_date = search_string[index+4:]
                exp_date2 = search_string[index+4:index+8]
                numeric = 0
                for i in exp_date:
                    if i.isdigit():
                        numeric += 1
                        #print(numeric)
                    else:
                        break
                if numeric == 4:
                    if 2020 <= int(exp_date2) <= 2030:
                        key_counter += 1
                else:
                    print("Wrong expiration date (2020-2030)")

            if "hgt" in search_string:
                index = search_string.index("hgt")
                #print(index)
                if "cm" in search_string:
                    height_cm = search_string[index + 4:]
                    height_cm2 = search_string[index + 4:index + 7]
                    numeric = 0
                    for i in height_cm:
                        if i.isdigit():
                            numeric += 1
                            print(numeric)
                        else:
                            break
                    if numeric == 3:
                        if 150 <= int(height_cm2) <= 193:
                            key_counter += 1
                    else:
                        print("Wrong height in cm (150 - 193)")

                elif "in" in search_string:
                    height_in = search_string[index + 4:]
                    height_in2 = search_string[index + 4: index + 6]
                    numeric = 0
                    for i in height_in:
                        if i.isdigit():
                            numeric += 1
                            print(numeric)
                        else:
                            break
                    if numeric == 2:
                        if 59 <= int(height_in2) <= 76:
                            key_counter += 1
                    else:
                        print("Wrong height in IN")
            if "ecl" in search_string:
                index = search_string.index("ecl")
                eye_color = search_string[index+4:index+7]
                #print(eye_color)
                if eye_color == "amb" or "blu" or "brn" or "gry" or "grn" or "hzl" or "oth":
                    key_counter += 1
                else:
                    print("Wrong eye color")

            if "pid" in search_string:
                index = search_string.index("pid")
                #passport_id = search_string[index+4:index+13]
                passport_id2 = search_string[index+4:]
                #print(passport_id)
                numeric = 0
                for i in passport_id2:
                    if i.isdigit():
                       numeric += 1
                       #print(numeric)
                    else:
                        break

                if numeric == 9:
                    key_counter += 1
                else:
                    print("Wrong passport ID")

            if "hcl" in search_string:
                index = search_string.index("hcl")
                hair_color = search_string[index+4:index+11]
                #print(hair_color)
                if hair_color[0] == "#":
                    pattern = re.compile("[a-f0-9]+")
                    #print(hair_color[1:7])
                    if pattern.fullmatch(hair_color[1:7]) is not None:
                        key_counter += 1
                        # print("validation")
                else:
                    print("Wrong hair color")
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
import re
with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

# print(list_input)


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
                numeric = 0
                for i in birthday_date:
                    if i.isdigit():
                       numeric += 1
                    else:
                        break
                if numeric == 4:
                    if 1920 <= int(birthday_date[0:4]) <= 2002:
                        key_counter += 1
                        print("Birthday year OK! 1920<=" + birthday_date[0:4] + "<=2002")
                    else:
                        print("Wrong birthday year value 1920<=" + birthday_date[0:4] + "<=2002")
                else:
                    print("Wrong birthday year (wrong data)")

            if "iyr" in search_string:
                index = search_string.index("iyr")
                issue_date = search_string[index+4:]

                numeric = 0
                for i in issue_date:
                    if i.isdigit():
                        numeric += 1
                    else:
                        break
                if numeric == 4:
                    if 2010 <= int(issue_date[0:4]) <= 2020:
                        key_counter += 1
                        print("Issue year OK! 2010<=" + issue_date[0:4] + "<=2020")
                    else:
                        print("Wrong issue year value 2010<=" + issue_date[0:4] + "<=2020")
                else:
                    print("Wrong issue year (data)")

            if "eyr" in search_string:
                index = search_string.index("eyr")
                exp_date = search_string[index+4:]
                numeric = 0
                for i in exp_date:
                    if i.isdigit():
                        numeric += 1
                    else:
                        break
                if numeric == 4:
                    if 2020 <= int(exp_date[0:4]) <= 2030:
                        key_counter += 1
                        print("Exp year OK! 2020<=" + exp_date[0:4] + "<=2030")
                    else:
                        print("Wrong exp year value 2020<=" + exp_date[0:4] + "<=2030")
                else:
                    print("Wrong expiration date (data)")

            if "hgt" in search_string:
                index = search_string.index("hgt")
                if "cm" in search_string:
                    height_cm = search_string[index + 4:]
                    numeric = 0
                    for i in height_cm:
                        if i.isdigit():
                            numeric += 1
                        else:
                            break
                    if numeric == 3:
                        if 150 <= int(height_cm[0:3]) <= 193:
                            key_counter += 1
                            print("Height CM OK! 150<=" + height_cm[0:3] + "<=193")
                        else:
                            print("Wrong height CM value 150<=" + height_cm[0:3] + "<=193")
                    else:
                        print("Wrong height in CM (data)")

                elif "in" in search_string:
                    height_in = search_string[index + 4:]
                    numeric = 0
                    for i in height_in:
                        if i.isdigit():
                            numeric += 1
                        else:
                            break
                    if numeric == 2:
                        if 59 <= int(height_in[0:2]) <= 76:
                            key_counter += 1
                            print("Height IN OK! 59<=" + height_in[0:2] + "<=76")

                    else:
                        print("Wrong height CM value 59<=" + height_in[0:2] + "<=76")
                else:
                    print("Wrong height in IN (data)")

            if "ecl" in search_string:
                index = search_string.index("ecl")
                eye_color = search_string[index+4:index+7]
                if eye_color == "amb" or eye_color == "blu" or eye_color == "brn" or eye_color == "gry" or \
                        eye_color == "grn" or eye_color == "hzl" or eye_color == "oth":
                    key_counter += 1
                    print("Eye color OK! " + eye_color)
                else:
                    print("Wrong eye color")

            if "pid" in search_string:
                index = search_string.index("pid")
                passport_id = search_string[index+4:]
                numeric = 0
                for i in passport_id:
                    if i.isdigit():
                       numeric += 1
                    else:
                        break
                if numeric == 9:
                    key_counter += 1
                    print("Passport ID OK! " + passport_id[0:9])

                else:
                    print("Wrong passport ID!")

            if "hcl" in search_string:
                index = search_string.index("hcl")
                hair_color = search_string[index+4:index+11]
                if hair_color[0] == "#":
                    pattern = re.compile("[0-9a-f]{6}$")
                    if pattern.fullmatch(hair_color[1:7]) is not None:
                        key_counter += 1
                        print("Hair color OK! -> " + hair_color[0:7])
                else:
                    print("Wrong hair color (data)")

        else:
            if key_counter >= 7: #should be 7
                print("PASSPORT VALID")
                passport_rate += 1
                print("Passport count:", passport_rate)
                print("\r")

            else:
                print("PASSPORT INVALID")
                passport_rate = passport_rate
                print("\r")


            key_counter = 0
            m += 1
        n += 1


passport_checker(list_input)
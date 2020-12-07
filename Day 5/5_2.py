with open('input.txt') as f:
    list_input = [line for line in f.read().splitlines()]

seat_id_list = []
def seats_checker(L):
    n = 0
    m = 0

    for x in L:

        search_seat = list_input[n]
        #print(search_seat)

        seats_pools = []
        column_pools = []
        seats_pools.extend(range(0, 128))
        column_pools.extend(range(0, 8))

        for y in search_seat:
            #print(m)
            if search_seat[m] == "F":
                seats_pools = seats_pools[:len(seats_pools) // 2]
                #print(seats_pools)
                m += 1

            elif search_seat[m] == "B":
                seats_pools = seats_pools[len(seats_pools) // 2:]
                #print(seats_pools)
                m += 1

            elif search_seat[m] == "L":
                column_pools = column_pools[:len(column_pools) // 2]
                #print(column_pools)
                m += 1

            elif search_seat[m] == "R":
                column_pools = column_pools[len(column_pools) // 2:]
                #print(column_pools)
                m += 1

            if m == 10:
                #print(seats_pools, column_pools)
                seat_id_list.append((int(seats_pools[0])*8)+int(column_pools[0]))
                n += 1
                m = 0

    print(seat_id_list)
    return seat_id_list

def highest_id(ID_list):
    print("Max ID: " + str(max(ID_list)))
    return max(ID_list)

def min_id(ID_list):
    print("Min ID: " + str(min(ID_list)))
    return min(ID_list)

seats_checker(list_input)
highest_id(seat_id_list)
min_id(seat_id_list)

sorted_list = []
sorted_list.extend(range(80, 927))
# print(sorted_list)

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

diff_list = (Diff(seat_id_list, sorted_list))

for x in diff_list:
    n = 0
    number = diff_list[n]
    if number < 70:
        diff_list.remove(number)
        n += 1
    print("Your seat is: " + str(diff_list[0]))
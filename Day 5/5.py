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

seats_checker(list_input)
highest_id(seat_id_list)



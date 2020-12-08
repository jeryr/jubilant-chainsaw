import advent_of_code_data as data

boarding = data.d5_input

def row(boarding):
    boarding = boarding[:7]
    row = [i for i in range(128)]
    for letter in boarding:
        cut = int(len(row)/2)
        if letter == "B":
            row = row[cut:]
        else:
            row = row[:cut]
    return row[0]



def column(boarding):
    boarding = boarding[7:]
    column = [i for i in range(8)]
    for letter in boarding:
        cut = int(len(column)/2)
        if letter == "R":
            column = column[cut:]
        else:
            column = column[:cut]
    return column[0]

def max_seat_id(seats):
    max_seat = 0
    seat_ids = []
    for seat in seats:
        seat_id = seat[0]*8 + seat[1]
        if seat_id > max_seat:
            max_seat = seat_id
    return max_seat

def seat_id(seats):
    seat_ids = []
    for seat in seats:
        seat_id = seat[0]*8 + seat[1]
        if seat_id > max_seat:
            max_seat = seat_id
    return max_seat

def boarding_complete(boarding):
    seats = []
    for boarding in boarding:
        seat = []
        seat.append(row(boarding))
        seat.append(column(boarding))
        seats.append(seat)
    
    print(max_seat_id(seats))
    return seats

def boarding_id(seats):
    id_list = [seat[0]*8 + seat[1] for seat in seats]
    id_list.sort()
    all_ids = [i for i in range(id_list[0], id_list[-1]+1)]
    for i in range(len(all_ids)):
        if id_list[i] != all_ids[i]:
            print(all_ids[i])
            break


boarding_id(boarding_complete(boarding))






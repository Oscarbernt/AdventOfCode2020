import functools

def find_seat_ids(boarding_passes):
    seat_ids = []
    highest_seatid = 0
    rules = {
        'F': lambda a: a[:len(a)//2],
        'B': lambda a: a[len(a)//2:],
        'R': lambda a: a[len(a)//2:],
        'L': lambda a: a[:len(a)//2],
    }
    for boarding_pass in boarding_passes:
        seats = list(range(128))
        for letter in boarding_pass[:7]:
            seats = rules[letter](seats)
        seat_row = seats[0]
        
        seats = list(range(8))
        for letter in boarding_pass[7:]:
            seats = rules[letter](seats)
        seat_column = seats[0]

        current_seat_id = seat_row * 8 + seat_column
        seat_ids.append(current_seat_id)

    return seat_ids

def get_boarding_passes():
    file = open("puzzle_input.txt", "r")
    return file.read().splitlines()

def find_my_seat_id(seat_ids):
    seat_ids.sort()
    lowest_seat_id = seat_ids[0] 
    while(True):
        if lowest_seat_id not in seat_ids and lowest_seat_id + 1 in seat_ids and lowest_seat_id - 1 in seat_ids:
            print("This is the match:", lowest_seat_id)
            break
        lowest_seat_id += 1

if __name__ == "__main__":
    boarding_passes = get_boarding_passes()
    seat_ids = find_seat_ids(boarding_passes)
    find_my_seat_id(seat_ids)
    
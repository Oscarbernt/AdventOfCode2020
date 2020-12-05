def find_highest_seat_id(boarding_passes):
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
        if highest_seatid < current_seat_id:
            highest_seatid = current_seat_id

    print(highest_seatid)

def get_boarding_passes():
    file = open("puzzle_input.txt", "r")
    return file.read().splitlines()

if __name__ == "__main__":
    boarding_passes = get_boarding_passes()
    seat_ids = find_highest_seat_id(boarding_passes)


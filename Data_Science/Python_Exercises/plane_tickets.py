def generate_seat_letters(number):
    letters = ["A", "B", "C", "D"]
    total_letters = 0
    i = 0
    while total_letters < number:
        yield letters[i]
        total_letters += 1
        i += 1
        if i >= len(letters):
            i = 0

def generate_seats(number):
    i = 1
    for letter in generate_seat_letters(number):
        yield f"{i}{letter}"
        if letter == "D":
            i += 1
            if i == 13:
                i += 1

def assign_seats(passengers):
    assigned_seats = {}
    seats = generate_seats(len(passengers))
    for name in passengers:
        assigned_seats[name] = next(seats)

    return assigned_seats

def generate_codes(seat_numbers, flight_id):
    for seat_number in seat_numbers:
        code_string = f"{seat_number}{flight_id}"
        yield code_string + ("0" * (12 - len(code_string)))
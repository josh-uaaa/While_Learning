def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        if number == 1:
            return 1
        else:
            return 2 ** (number - 1)

def total():
    total_grains = 0
    total_squares = 64
    while total_squares != 0:
        total_grains += square(total_squares)
        total_squares -= 1

    return total_grains
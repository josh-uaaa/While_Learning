def square_of_sum(number):
    result = 0
    for i in range(number + 1):
        result += i
    result *= result

    return result

def sum_of_squares(number):
    result = 0
    for i in range(number + 1):
        result += (i * i)

    return result

def difference_of_squares(number):
    return abs(square_of_sum(number) - sum_of_squares(number))
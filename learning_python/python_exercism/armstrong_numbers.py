def is_armstrong_number(number):
    power = count_digits(number)
    temp = number
    sum = 0
    while temp > 0:
        digit = temp % 10             # Gets the last digit of the number.
        sum += (digit ** power)
        temp //= 10                   # Removes the last digit of the number.

    return sum == number

def count_digits(number):
    count = 0
    temp = number
    while temp > 0:
        temp //= 10                   # Removes the last digit of the number.
        count += 1

    return count
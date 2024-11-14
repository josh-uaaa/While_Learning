def square_root(number):
    left, right = 1, number
    middle = (left + right) // 2
    while left <= right:
        sqrt_answer = middle * middle
        if sqrt_answer == number:
            break
        elif sqrt_answer > number:
            right = middle - 1
            middle = (left + right) // 2
        else:
            left = middle + 1
            middle = (left + right) // 2

    return middle
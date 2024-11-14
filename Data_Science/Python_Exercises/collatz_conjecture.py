def steps(number):
    steps_required = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number != 1:
            if (number % 2) == 0:
                number = number // 2
            else:
                number = (number * 3) + 1
            steps_required += 1

    return steps_required
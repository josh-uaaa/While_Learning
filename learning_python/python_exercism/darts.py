import math

def score(x, y):
    dart_location = math.sqrt((x * x) + (y * y))
    if dart_location <= 1:
        return 10
    elif 1 < dart_location <= 5:
        return 5
    elif 5 < dart_location <= 10:
        return 1
    else:
        return 0
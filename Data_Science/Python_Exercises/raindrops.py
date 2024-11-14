def convert(number):
    result_string = ""
    if number % 3 == 0:
        result_string = result_string + "Pling"
    if number % 5 == 0:
        result_string = result_string + "Plang"
    if number % 7 == 0:
        result_string = result_string + "Plong"
    if len(result_string) == 0:
        result_string = str(number)

    return result_string
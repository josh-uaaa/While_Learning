def is_valid(isbn):
    isbn_digits = []
    for i, char in enumerate(isbn):
        if char.isnumeric() and i < len(isbn):
            isbn_digits.append(int(char))
        elif i == len(isbn) - 1 and char == "X":
            isbn_digits.append(10)
        elif char.isalpha() and i < len(isbn):
            return False

    if len(isbn_digits) == 10:
        mult_digit = 10
        formula_result = 0
        for digit in isbn_digits:
            formula_result += digit * mult_digit
            mult_digit -= 1
        return formula_result % 11 == 0

    return False
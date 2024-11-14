def is_isogram(string):
    string = string.lower()
    present_letters = []
    for char in string:
        if char.isalpha():
            if char not in present_letters:
                present_letters.append(char)
            else:
                return False

    return True
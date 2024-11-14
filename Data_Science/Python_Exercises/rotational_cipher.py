def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotated_alphabet = alphabet[key:] + alphabet[0:key]
    rotated_dict = {}
    for i, letter in enumerate(rotated_alphabet):
        rotated_dict[alphabet[i]] = letter

    result_string = ""
    for character in text:
        if character.isalpha():
            if character.isupper():
                result_string = result_string + rotated_dict[character.lower()].upper()
            else:
                result_string = result_string + rotated_dict[character]
        else:
            result_string = result_string + character

    return result_string
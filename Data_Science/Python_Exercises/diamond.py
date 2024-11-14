ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rows(letter):
    diamond = []

    letter_index = ALPHABET.index(letter)
    diamond_string = f'{ALPHABET[letter_index::-1]}{ALPHABET[1:letter_index + 1]}'
    curr_string = ''
    for letter in ALPHABET[:letter_index + 1]:
        for curr_letter in diamond_string:
            if curr_letter == letter:
                curr_string += curr_letter
            else:
                curr_string += ' '
        diamond.append(curr_string)
        curr_string = ''

    if len(diamond) > 1:
        lower_half = diamond[len(diamond) - 2::-1]
        diamond.extend(lower_half)

    return diamond
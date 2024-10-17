PLAIN_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
CIPHER_ALPHABET = PLAIN_ALPHABET[::-1]

def encode(plain_text):
    encoded_text = []

    curr_group = ''
    for char in plain_text.lower():
        if char.isalnum():
            if char in PLAIN_ALPHABET:
                char = CIPHER_ALPHABET[PLAIN_ALPHABET.index(char)]
            if len(curr_group) == 5:
                encoded_text.append(curr_group)
                curr_group = ''
            curr_group += char
    encoded_text.append(curr_group)

    return ' '.join(encoded_text)

def decode(ciphered_text):
    decoded_text = ''
    for char in ciphered_text:
        if char.isalnum():
            if char in PLAIN_ALPHABET:
                char = PLAIN_ALPHABET[CIPHER_ALPHABET.index(char)]
            decoded_text += char

    return decoded_text
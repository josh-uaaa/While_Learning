import random
import string

class Cipher:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, key=None):
        if not key:
            self.key = self.generate_key()
        else:
            self.key = key

    def encode(self, text):
        encoded_text = ""

        curr_key_index = 0
        for letter in text:
            distance_from_a = Cipher.alphabet.index(letter)
            encoded_char_index = Cipher.alphabet.index(self.key[curr_key_index])

            # Cycle through alphabet, landing on the target character, a distance away from 'a'.
            while distance_from_a > 0:
                encoded_char_index += 1
                if encoded_char_index >= 26:
                    encoded_char_index = 0
                distance_from_a -= 1
            encoded_text += Cipher.alphabet[encoded_char_index]

            # Cycle through key, ensuring that it does not go out of bounds.
            curr_key_index += 1
            if curr_key_index >= len(self.key):
                curr_key_index = 0

        return encoded_text

    def decode(self, text):
        decoded_text = ""

        curr_key_index = 0
        for letter in text:
            # Cycle through alphabet until curr_char == letter, keep track of distance travelled.
            distance_between = 0
            curr_index = Cipher.alphabet.index(self.key[curr_key_index])
            curr_char = Cipher.alphabet[curr_index]
            while curr_char != letter:
                curr_index += 1
                if curr_index >= 26:
                    curr_index = 0
                distance_between += 1
                curr_char = Cipher.alphabet[curr_index]
            decoded_text += Cipher.alphabet[distance_between]

            # Cycle through key, ensuring that it does not go out of bounds.
            curr_key_index += 1
            if curr_key_index >= len(self.key):
                curr_key_index = 0

        return decoded_text

    def generate_key(self):
        return "".join(random.choices(string.ascii_lowercase, k=100))
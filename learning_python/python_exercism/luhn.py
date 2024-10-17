class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card_string = ''.join(str(self.card_num).split())

        if len(card_string) <= 1:
            return False

        cleaned_card = ""
        for char in card_string:
            if not char.isdigit():
                return False
            else:
                cleaned_card += char

        reversed_cleaned = cleaned_card[::-1]
        sum_of_digits = 0
        for i in range(0, len(reversed_cleaned)):
            curr_digit = int(reversed_cleaned[i])
            if (i + 1) % 2 == 0:
                curr_digit = ((curr_digit * 2) - 9) if (curr_digit * 2) > 9 else (curr_digit * 2)
            sum_of_digits += curr_digit

        return sum_of_digits % 10 == 0
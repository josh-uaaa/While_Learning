class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]

    def clean_number(self, number):
        valid_punctuations = "+()-. "
        cleaned_number = ""
        for char in number:
            if char.isalpha():
                raise ValueError("letters not permitted")
            elif char not in valid_punctuations:
                if char.isdigit():
                    cleaned_number += char
                else:
                    raise ValueError("punctuations not permitted")
        if self.validate_number(cleaned_number):
            if len(cleaned_number) == 11:
                cleaned_number = cleaned_number[1:]
            return cleaned_number
        else:
            raise ValueError("Invalid phone number")

    def validate_number(self, number):
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(number) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(number) == 11:
            area_code, exchange_code = number[1:4], number[4:7]
            if number[0] != "1":
                raise ValueError("11 digits must start with 1")
        elif len(number) == 10:
            area_code, exchange_code = number[0:3], number[3:6]

        if exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        elif exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")

        if area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        elif area_code[0] == "1":
            raise ValueError("area code cannot start with one")

        return True

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
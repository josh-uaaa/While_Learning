ONES_TEENS = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
              "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
TENS = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
SCALES = {1e9: 'billion', 1e6: 'million', 1e3: 'thousand', 1e2: 'hundred'}

def say(number):
    stringified_number = ""

    if number > 999_999_999_999 or number < 0:
        raise ValueError("input out of range")

    if number == 0:
        return ONES_TEENS[number]

    broken_down = []
    for scale, scale_word in SCALES.items():
        if number >= scale:
            broken_down.append(say(int(number // scale)))
            broken_down.append(scale_word)
            number = int(number % scale)

    curr_string = ""
    if number >= 20:
        curr_string += TENS[number // 10]
        number = int(number % 10)
        if number:
            curr_string += "-"
    if number and number < 20:
        curr_string += ONES_TEENS[number]
    if curr_string:
        broken_down.append(curr_string)

    stringified_number = " ".join(broken_down)
    return stringified_number
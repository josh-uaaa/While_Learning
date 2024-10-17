def decode(string):
    decoded_string = ""

    if len(string) <= 1:
        return string
    else:
        curr_char, curr_run_count = string[0], ""
        if curr_char.isdigit():
            curr_run_count += curr_char
        else:
            decoded_string += curr_char

        for char in string[1:]:
            if char.isdigit():
                curr_run_count += char
            else:
                if not curr_run_count:
                    decoded_string += char
                else:
                    decoded_string += f"{char * int(curr_run_count)}"
                curr_run_count = ""

    return decoded_string

def encode(string):
    encoded_string = ""

    if len(string) <= 1:
        return string
    else:
        curr_char, curr_run_count = string[0], 1
        for char in string[1:]:
            if char == curr_char:
                curr_run_count += 1
            else:
                if curr_run_count == 1:
                    encoded_string += curr_char
                else:
                    encoded_string += f"{curr_run_count}{curr_char}"
                curr_char, curr_run_count = char, 1

        if curr_run_count == 1:
            encoded_string += curr_char
        else:
            encoded_string += f"{curr_run_count}{curr_char}"

    return encoded_string
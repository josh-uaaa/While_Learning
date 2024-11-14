def value(colors):
    colors_list = {"black": "0", "brown": "1", "red": "2", "orange": "3", "yellow": "4", "green": "5", "blue": "6", "violet": "7", "grey": "8", "white": "9"}
    final_value = ""
    for c in colors:
        final_value = final_value + colors_list[c]
        if len(final_value) == 2:
            break

    return int(final_value)
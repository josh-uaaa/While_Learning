def color_code(color):
    colors_list = colors()
    for i, c in enumerate(colors_list):
        if color == c:
            return i

def colors():
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return colors
COLORS_TUPLE = ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white')
TOLERANCES = {'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%', 'green': '0.5%', 'brown': '1%', 'red': '2%', 'gold': '5%', 'silver': '10%'}

def resistor_label(colors):
    resistor_value = 0
    if len(colors) == 4:
        a, b, multiplier, tolerance = colors[0], colors[1], colors[2], colors[3]
        resistor_value = ((10 * color_value(a)) + color_value(b)) * (10 ** color_value(multiplier))
    elif len(colors) == 5:
        a, b, c, multiplier, tolerance = colors[0], colors[1], colors[2], colors[3], colors[4]
        resistor_value = ((100 * color_value(a)) + (10 * color_value(b)) + color_value(c)) * (10 ** color_value(multiplier))
    else:
        return "0 ohms"

    metric_prefix = ""
    if resistor_value >= (10 ** 9):
        metric_prefix = "giga"
        resistor_value /= (10 ** 9)
    elif resistor_value >= (10 ** 6):
        metric_prefix = "mega"
        resistor_value /= (10 ** 6)
    elif resistor_value >= (10 ** 3):
        metric_prefix = "kilo"
        resistor_value /= (10 ** 3)

    return f"{resistor_value:g} {metric_prefix}ohms ±{TOLERANCES[tolerance]}"

def color_value(band_color):
    return COLORS_TUPLE.index(band_color)
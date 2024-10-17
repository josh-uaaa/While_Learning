COLORS_TUPLE = ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white')

def label(colors):
    a, b, multiplier = colors[0], colors[1], colors[2]
    resistor_value = ((10 * COLORS_TUPLE.index(a)) + COLORS_TUPLE.index(b)) * (10 ** COLORS_TUPLE.index(multiplier))

    metric_prefix = ""
    if resistor_value > (10 ** 9):
        metric_prefix = "giga"
        resistor_value //= (10 ** 9)
    elif resistor_value > (10 ** 6):
        metric_prefix = "mega"
        resistor_value //= (10 ** 6)
    elif resistor_value > (10 ** 3):
        metric_prefix = "kilo"
        resistor_value //= (10 ** 3)

    return f"{resistor_value} {metric_prefix}ohms"
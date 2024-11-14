def is_critically_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500_000

def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage = ((voltage * current) / theoretical_max_power) * 100

    band_color = ''
    if percentage >= 80:
        band_color = 'green'
    elif 80 > percentage >= 60:
        band_color = 'orange'
    elif 60 > percentage >= 30:
        band_color = 'red'
    else:
        band_color = 'black'

    return band_color

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    value = temperature * neutrons_produced_per_second

    if value < (threshold * 0.90):
        status_code = 'LOW'
    elif (threshold - (threshold * 0.10)) < value < (threshold + (threshold * 0.10)):
        status_code = 'NORMAL'
    else:
        status_code = 'DANGER'

    return status_code
from collections import Counter

def egg_count(display_value):
    temp_list = []
    curr_binary = 1
    while curr_binary <= display_value:
        temp_list = [curr_binary] + temp_list
        curr_binary *= 2

    binary_list = []
    for value in temp_list:
        if display_value >= value:
            display_value -= value
            binary_list.append(1)
        else:
            binary_list.append(0)

    return Counter(binary_list)[1]
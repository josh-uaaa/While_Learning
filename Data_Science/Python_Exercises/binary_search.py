def find(search_list, value):
    left_index, right_index = 0, len(search_list) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        current_element = search_list[middle_index]
        if current_element == value:
            return middle_index
        elif current_element < value:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    raise ValueError("value not in array")
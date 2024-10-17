def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    slices_list = []
    final_index = length
    while final_index <= len(series):
        curr_slice = series[final_index - length:final_index]
        slices_list.append(curr_slice)
        final_index += 1

    return slices_list
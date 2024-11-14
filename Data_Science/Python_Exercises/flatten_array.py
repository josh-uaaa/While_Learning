def flatten(iterable):
    flattened_array = []
    for item in iterable:
        if item is not None:
            if type(item) is list:
                flattened_array.extend(flatten(item))
            else:
                flattened_array.append(item)

    return flattened_array
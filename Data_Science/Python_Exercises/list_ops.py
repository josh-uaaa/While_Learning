def append(list1, list2):
    return list1 + list2


def concat(lists):
    flattened_list = []
    for element in lists:
        flattened_list = append(flattened_list, element)
    return flattened_list


def filter(function, list):
    true_list = []
    for element in list:
        if function(element):
            true_list = append(true_list, [element])

    return true_list

def length(list):
    list_length = 0
    for element in list:
        list_length += 1

    return list_length

def map(function, list):
    results_list = []
    for element in list:
        results_list = append(results_list, [function(element)])

    return results_list

def foldl(function, list, initial):
    for element in list:
        initial = function(initial, element)
    return initial

def foldr(function, list, initial):
    return foldl(function, reverse(list), initial)

def reverse(list):
    return list[::-1]
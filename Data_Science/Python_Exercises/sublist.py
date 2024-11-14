SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif check_sublist(list_one, list_two):
        return SUBLIST
    elif check_sublist(list_two, list_one):
        return SUPERLIST

    return UNEQUAL

def check_sublist(sublist, superlist):
    if not sublist:
        return True
    elif len(sublist) < len(superlist):
        for index, val in enumerate(superlist):
            if (val == sublist[0]) and superlist[index:len(sublist) + index] == sublist:
                return True

    return False
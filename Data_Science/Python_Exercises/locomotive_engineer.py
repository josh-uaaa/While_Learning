def get_list_of_wagons(*args):
    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    a, b, c, *rest = each_wagons_id
    wagons_list = get_list_of_wagons(c, *missing_wagons, *rest, a, b)

    return wagons_list

def add_missing_stops(route, **kwargs):
    stops_list = list(kwargs.values())
    route["stops"] = stops_list
    return route

def extend_route_information(route, more_route_information):
    extended_route_info = {**route, **more_route_information}
    return extended_route_info

def fix_wagon_depot(wagons_rows):
    wagon_rows_list = []
    zipped_rows = zip(*wagons_rows)
    for row in zipped_rows:
        wagon_rows_list.append(list(row))

    return wagon_rows_list
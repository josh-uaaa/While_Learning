def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    azara_coordinate = get_coordinate(azara_record)
    return convert_coordinate(azara_coordinate) in rui_record

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        new_record = azara_record + rui_record
        return tuple(new_record)

    return "not a match"

def clean_up(combined_record_group):
    return "".join(f"{(record[0], record[2], record[3], record[4])}\n" for record in combined_record_group)
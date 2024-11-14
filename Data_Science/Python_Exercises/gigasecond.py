from datetime import timedelta

GIGA_SECOND = 1e9

def add(moment):
    return moment + timedelta(seconds=GIGA_SECOND)
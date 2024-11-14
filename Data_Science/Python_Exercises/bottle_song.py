NUMBERS = ["no", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

def recite(start, take=1):
    verses, curr_verse = [], ""
    while take > 0:
        verses.append(f"{NUMBERS[start]} green bottle{'s' if start > 1 else ''} hanging on the wall,")
        verses.append(f"{NUMBERS[start]} green bottle{'s' if start > 1 else ''} hanging on the wall,")
        verses.append(f"And if one green bottle should accidentally fall,")
        start -= 1
        verses.append(f"There'll be {NUMBERS[start].lower()} green bottle{'s' if start != 1 else ''} hanging on the wall.")
        if take != 1:
            verses.append("")
        take -= 1
    return verses
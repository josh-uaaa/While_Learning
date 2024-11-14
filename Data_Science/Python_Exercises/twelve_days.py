NTH_DAY = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth",
          "tenth", "eleventh", "twelfth")
GIFTS = ("a Partridge in a Pear Tree.",
        "two Turtle Doves, and ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ")

def recite(start_verse, end_verse):
    verses_list = []
    for i in range(start_verse - 1, end_verse):
        curr_verse = f"On the {NTH_DAY[i]} day of Christmas my true love gave to me: "
        for j in range(i, -1, -1):
            curr_verse += GIFTS[j]
        verses_list.append(curr_verse)

    return verses_list
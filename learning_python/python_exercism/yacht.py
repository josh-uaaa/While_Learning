YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    if category == 0:
        if len(set(dice)) == 1:
            return 50
        return 0

    if category in [1, 2, 3, 4, 5, 6]:
        return sum(value for value in dice if value == category)

    if category == 7:
        if len(set(dice)) == 2 and any(dice.count(value) == 3 for value in set(dice)):
            return sum(dice)
        return 0

    if category == 8:
        for value in set(dice):
            if dice.count(value) >= 4:
                return value * 4
        return 0

    if category == 9:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        return 0

    if category == 10:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        return 0

    if category == 11:
        return sum(dice)
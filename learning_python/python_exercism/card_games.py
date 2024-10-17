def get_rounds(number):
    return list([number, number + 1, number + 2])

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    hand_sum = 0
    for number in hand:
        hand_sum += number

    return hand_sum / len(hand)

def approx_average_is_average(hand):
    calculated_average = sum(hand) / len(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[(len(hand) // 2)]

    return calculated_average in (first_last_average, middle_card)

def average_even_is_average_odd(hand):
    even_sum, even_count, odd_sum, odd_count = 0, 0, 0, 0
    for index, number in enumerate(hand):
        if index % 2 == 0:
            even_sum += number
            even_count += 1
        else:
            odd_sum += number
            odd_count += 1

    return (even_sum / even_count) == (odd_sum / odd_count)

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand = hand[:-1] + [22]

    return hand
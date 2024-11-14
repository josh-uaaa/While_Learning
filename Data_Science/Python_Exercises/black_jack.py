def value_of_card(card):
    face_cards = ('J', 'Q', 'K')

    if card in face_cards:
        card_value = 10
    elif card == 'A':
        card_value = 1
    else:
        card_value = int(card)

    return card_value

def higher_card(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value > card_two_value:
        higher_value = card_one
    elif card_two_value > card_one_value:
        higher_value = card_two
    else:
        higher_value = (card_one, card_two)

    return higher_value

def value_of_ace(card_one, card_two):
    if card_one == 'A' or card_two == 'A':
        ace_value = 1
    else:
        current_hand_value = value_of_card(card_one) + value_of_card(card_two)
        ace_one = current_hand_value + 1
        ace_eleven = current_hand_value + 11

        if ace_one <= 21 and ace_eleven <= 21:
            if ace_one < ace_eleven:
                ace_value = 11
            else:
                ace_value = 1
        elif ace_eleven <= 21:
            ace_value = 11
        else:
            ace_value = 1

    return ace_value

def is_blackjack(card_one, card_two):
    ten_cards = ('10', 'K', 'Q', 'J')

    blackjack_hand = False
    if card_one in ten_cards:
        if card_two == 'A':
            blackjack_hand = True
    elif card_two in ten_cards:
        if card_one == 'A':
            blackjack_hand = True
    else:
        blackjack_hand = False

    return blackjack_hand

def can_split_pairs(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    return card_one_value == card_two_value

def can_double_down(card_one, card_two):
    eligible_points = (9, 10, 11)
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    value_in_hand = card_one_value + card_two_value

    return value_in_hand in eligible_points
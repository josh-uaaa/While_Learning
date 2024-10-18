STRAIGHT_FLUSH = 8
FOUR_OF_A_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

class Hand:
    valid_ranks = "--234567890JQKA"

    def __init__(self, hand):
        self.hand = hand

        ranks, suits = [], set()
        for card in self.hand.split():
            ranks.append(Hand.valid_ranks.index(card[-2]))
            suits.add(card[-1])
        ranks.sort(reverse=True)
        ranks = [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks
        rank_counts = [(ranks.count(rank), rank) for rank in set(ranks)]
        rank_counts.sort(reverse=True)

        self.group, self.numbers = zip(*rank_counts)
        self.flush = len(suits) == 1
        self.straight = len(self.group) == 5 and (max(ranks) - min(ranks) == 4)

    def score_hand(self):
        hand_score = HIGH_CARD
        if self.straight and self.flush:
            hand_score = STRAIGHT_FLUSH
        elif self.group == (4, 1):
            hand_score = FOUR_OF_A_KIND
        elif self.group == (3, 2):
            hand_score = FULL_HOUSE
        elif self.flush:
            hand_score = FLUSH
        elif self.straight:
            hand_score = STRAIGHT
        elif self.group == (3, 1, 1):
            hand_score = THREE_OF_A_KIND
        elif self.group == (2, 2, 1):
            hand_score = TWO_PAIR
        elif self.group == (2, 1, 1, 1):
            hand_score = ONE_PAIR
        return hand_score, self.numbers

    def __eq__(self, other_hand):
        return self.score_hand() == other_hand.score_hand()


def best_hands(hands):
    hands_list = [Hand(hand) for hand in hands]
    hands_list.sort(key=lambda hand: hand.score_hand(), reverse=True)
    best_hand = hands_list[0]
    return [hand.hand for hand in hands_list if hand == best_hand]
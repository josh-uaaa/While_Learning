LETTER_SCORING = {('a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'): 1,
                  ('d', 'g'): 2,
                  ('b', 'c', 'm', 'p'): 3,
                  ('f', 'h', 'v', 'w', 'y'): 4,
                  ('k'): 5,
                  ('j', 'x'): 8,
                  ('q', 'z'): 10}

def score(word):
    word_score = 0
    for letter in word.lower():
        for letter_list, score in LETTER_SCORING.items():
            if letter in letter_list:
                word_score += score
                break

    return word_score
def find_anagrams(word, candidates):
    valid_anagrams = []

    letters_in_word = list(word.lower())
    for candidate in candidates:
        if len(candidate) == len(word) and candidate.lower() != word.lower():
            letters_in_candidate = list(candidate.lower())
            for letter in letters_in_word:
                if letter in letters_in_candidate:
                    letters_in_candidate.remove(letter)
            if len(letters_in_candidate) == 0:
                valid_anagrams.append(candidate)

    return valid_anagrams
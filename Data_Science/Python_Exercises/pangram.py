def is_pangram(sentence):
    sentence = sentence.lower()
    present_letters = []
    for char in sentence:
        if char.isalpha():
            present_letters.append(char)

    return len(set(present_letters)) == 26
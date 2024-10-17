import re

def count_words(sentence):
    word_count = {}

    cleaned_sentence = re.sub(r"(?!\b's\b|\b't\b|\b're\b)[^a-zA-Z0-9\s]", " ", sentence.lower())
    split_sentence = cleaned_sentence.split()
    for word in split_sentence:
        if word not in word_count.keys():
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count
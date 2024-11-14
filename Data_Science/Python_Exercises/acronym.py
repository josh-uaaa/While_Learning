import re

def abbreviate(words):
    abbreviation = ''
    cleaned_words = re.sub(r"[^a-zA-Z\s']", ' ', words)
    separated_words = cleaned_words.split()
    for word in separated_words:
        abbreviation += word[0].upper()

    return abbreviation
VOWELS = ('a', 'e', 'i', 'o', 'u')

def translate(text):
    pig_latin = []

    text = text.lower().split()
    for word in text:
        if (word[0] in VOWELS) or (word[:2] == 'xr') or (word[:2] == 'yt'):  # Rule One.
            pig_latin.append(f'{word}ay')
        else:
            starting_consonants = 0
            for letter in word:
                if letter not in VOWELS:
                    starting_consonants += 1
                else:
                    break
            if 'qu' in word[:starting_consonants + 1]:  # Rule Three.
                pig_latin.append(f'{word[starting_consonants + 1:]}{word[:starting_consonants + 1]}ay')
            elif 'y' in word[:starting_consonants + 1] and word[0] != 'y':  # Rule Four.
                y_index = word.index('y')
                pig_latin.append(f'{word[y_index:]}{word[:y_index]}ay')
            else:
                pig_latin.append(f'{word[starting_consonants:]}{word[:starting_consonants]}ay')

    return ' '.join(pig_latin)
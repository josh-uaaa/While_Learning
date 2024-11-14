def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    result = prefix + " :: "
    for word in vocab_words:
        if word != prefix:
            if word == vocab_words[-1]:
                result = result + prefix + word
            else:
                result = result + prefix + word + " :: "

    return result

def remove_suffix_ness(word):
    if word[-4:] == "ness":
        new_word = word[:-4]
        if new_word[-1] == "i":
            new_word = new_word[:-1] + "y"

    return new_word

def adjective_to_verb(sentence, index):
    words_in_sentence = sentence.split()
    verb = words_in_sentence[index]
    if verb.endswith("."):
        verb = verb[:-1]

    return verb + "en"
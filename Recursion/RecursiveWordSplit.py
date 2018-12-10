
def recursive_word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return recursive_word_split(phrase[len(word):], list_of_words, output)

    return output


str1 = 'iamJohn'
vocab = ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']
output = recursive_word_split(str1, vocab)
print(output)

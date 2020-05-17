
def detect_capital_use(word):
    """
    :type word: str
    :rtype: bool
    """
    size = len(word)
    count = 0

    for i in range(size):
        if word[i].isupper():
            count += 1

    if count == 0 or count == size:
        return True
    else:
        if count == 1 and word[0].isupper():
            return True

    return False

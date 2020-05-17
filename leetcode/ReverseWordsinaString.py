def reverse_words(s):
    """
    :type s: str
    :rtype: str
    """
    s = s.split()
    i = 0
    j = len(s) - 1

    while i <= j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return " ".join(s)

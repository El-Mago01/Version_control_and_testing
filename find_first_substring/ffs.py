def first_substr(word, char):
    """
    Find the index of the first occurrence of char in word.
    Returns -1 if char is not found.
    """
    for i in range(len(word)): 
        if word[i] == char:
            return i
    return -1
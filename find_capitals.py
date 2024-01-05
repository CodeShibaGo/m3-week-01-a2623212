def find_capitals(word):
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if type(word) is not str:
         return
    capital_words = ""
    for letter in word:
        if letter in capitals:
            capital_words += letter

    return capital_words

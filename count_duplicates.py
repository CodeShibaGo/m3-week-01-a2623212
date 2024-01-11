def count_duplicates(text):
    if type(text) is not str:
        return

    text = text.lower()
    text_unique = []
    text_again = []
    count = 0

    for char in text:
        if char not in text_unique:
            text_unique.append(char)
        elif char not in text_again:
            text_again.append(char)
            count += 1
    return count

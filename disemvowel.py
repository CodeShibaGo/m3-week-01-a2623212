def disemvowel(s):
    disemvowel_string = ""
    for char in s:
        if char not in 'aeiouAEIOU':
            disemvowel_string += char

    return disemvowel_string

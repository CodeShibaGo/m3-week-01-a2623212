def even_or_odd(number):
    if type(number) != int:
        return

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"



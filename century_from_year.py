def century(year):
    import math
    if year % 100 == 0:
        return math.floor(year / 100)
    else:
        return math.floor(year / 100 + 1)

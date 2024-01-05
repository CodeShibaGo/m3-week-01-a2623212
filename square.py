def is_square(n):
    import math
    if n < 0:
        return False

    sqrt = math.sqrt(n)
    return sqrt == int(sqrt)
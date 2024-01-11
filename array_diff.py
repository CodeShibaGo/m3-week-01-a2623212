def array_diff(a, b):
    if type(a) is not list or type(b) is not list:
        return

    b_set = set(b)
    return [item for item in a if item not in b_set]
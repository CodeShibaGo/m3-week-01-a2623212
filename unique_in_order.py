def unique_in_order(iterable):
    result = []
    for item in iterable:
        if item not in result or result[-1] != item:
            result.append(item)
    return result

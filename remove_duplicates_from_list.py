def distinct(seq):
    seen = []
    first_seen = []
    for item in seq:
        if item not in seen:
            seen.append(item)
            first_seen.append(item)
    return first_seen

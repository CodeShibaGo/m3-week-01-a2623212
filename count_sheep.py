def count_sheep(sheeps):
    if type(sheeps) is not list:
        return

    sleeping_sheep = []
    for sheep in sheeps:
        if sheep is True:
            sleeping_sheep.append(sheep)
    return len(sleeping_sheep)
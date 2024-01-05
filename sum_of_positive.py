def positive_sum(arr):
    if type(arr) is not list:
        return

    positive_num = []
    for i in arr:
        if type(i) is int and i >= 0:
            positive_num.append(i)

    return sum(positive_num)


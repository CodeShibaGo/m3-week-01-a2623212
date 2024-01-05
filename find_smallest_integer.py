def find_smallest_int(arr):
    for item in arr:
        if type(item) is not int:
            return
    tem_list = arr
    tem_list.sort()
    return tem_list[0]

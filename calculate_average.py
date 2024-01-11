def calculate_average(nums):
    if type(nums) is not list:
        return

    if len(nums) == 0:
        return 0

    return sum(nums)/len(nums)

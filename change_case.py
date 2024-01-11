def change_case(input_str, case):
    if type(input_str) != str:
        return
    if case == "upper":
        input_str = input_str.upper()
        return input_str
    elif case == "lower":
        input_str = input_str.lower()
        return input_str
    else:
        return



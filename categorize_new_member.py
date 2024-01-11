def categorize_new_member(data):
    if type(data) is not list:
        return
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        elif age < 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result
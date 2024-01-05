def greet(name):
    if type(name) is not str:
        return
    message = 'Hello, ' + name + '!'
    if name.lower() == "johnny":
        return 'Hello, my love!'
    else:
        return message
    
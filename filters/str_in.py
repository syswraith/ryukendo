def str_in(password, strings):
    default = False
    for x in strings:
        if x in password: default = True
    return default

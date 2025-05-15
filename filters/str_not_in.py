def str_not_in(password, strings):
    default = False
    for x in strings:
        if x not in password: default = True
    return default

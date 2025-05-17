def str_in(used, password, strings):
    if used:
        return any(x in password for x in strings)
    else:
        return True


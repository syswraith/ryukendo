def str_not_in(used, password, strings):
    if used:
        return all(x not in password for x in strings)
    else:
        return True


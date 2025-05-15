import filters as filters

with open('wordlist.txt', 'r') as file:
    for line in file:
        if filters.in_range(line, 1, 8): print(line, end='')

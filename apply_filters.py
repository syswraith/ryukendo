import filters as filters

def filter():

    range_start = int(input("Range start (inclusive): "))
    range_end= int(input("Range end (exclusive): "))
    is_str_in = True if input("string in filter (y/n): ") == 'y' else False
    is_str_not_in = True if input("string not in filter (y/n): ") == 'y' else False
    is_unique = True if input("string in filter (y/n): ") == 'y' else False
    
    if is_str_in: str_in_list = input("Input string in: ").split()
    if is_str_not_in: str_not_in_list = input("Input string not in: ").split()
    if is_unique: pass

    with open('wordlist.txt', 'r') as file:
    for line in file:
        if filters.in_range(line, start, end):

filter()

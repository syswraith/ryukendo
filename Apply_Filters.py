import filters

def filter():
    range_start = int(input("Range start (inclusive): "))
    range_end = int(input("Range end (exclusive): "))

    filters_to_apply = []

    if input("string in filter (y/n): ") == 'y':
        str_in_list = input("Input string in (separate with ,): ").split(',')
        filters_to_apply.append(lambda pwd: filters.str_in.str_in(True, pwd, str_in_list))

    if input("string not in filter (y/n): ") == 'y':
        str_not_in_list = input("Input string not in (separate with ,): ").split(',')
        filters_to_apply.append(lambda pwd: filters.str_not_in.str_not_in(True, pwd, str_not_in_list))

    with open('wordlist.txt', 'r') as file:
        for line in file:
            password = line.strip()
            if not filters.in_range.in_range(password, range_start, range_end):
                continue
            if all(f(password) for f in filters_to_apply):
                print(password)

filter()


import os
import json
from multiprocessing import Pool, cpu_count
from Person import Person

# Step 1: Extract max_mutuals and max_time_known
max_mutuals = max_time_known = 0
for x in os.listdir('./profiles/'):
    person = Person(f'./profiles/{x}', (max_mutuals, max_time_known))
    if person.extract_mutuals_and_time_known() > (max_mutuals, max_time_known):
        max_mutuals, max_time_known = person.extract_mutuals_and_time_known()

# Step 2: Build hierarchy
hierarchy = {}
for x in os.listdir('./profiles/'):
    if x == "target.json": continue
    person = Person(f'./profiles/{x}', (max_mutuals, max_time_known))
    hierarchy[x] = person.yield_closeness()
hierarchy_sorted = sorted(hierarchy, key=hierarchy.get, reverse=True)

# Step 3: Load target profile once
with open('profiles/target.json', 'r', encoding='utf-8') as f:
    target_data = json.load(f)

target = [
    (target_data["first_name"], target_data["middle_name"], target_data["last_name"]),
    tuple(str(x) for x in target_data["numbers"]),
    tuple(target_data["special_characters"])
]

# Step 4: Define worker
def process_person(filename):
    from Person import Person
    from Combinator import Combinator
    import json

    person = Person(f'./profiles/{filename}', (max_mutuals, max_time_known))
    other_person = person.yield_iterables()

    target_text = set(target[0] + other_person[0])
    target_numbers = set(target[1] + other_person[1])
    target_special_characters = set(target[2] + other_person[2])

    c1 = Combinator([target_text, target_numbers, target_special_characters])
    return list(c1.return_passwords())

# Step 5: Run multiprocessing
if __name__ == '__main__':
    with Pool(cpu_count()) as pool:
        all_password_lists = pool.map(process_person, hierarchy_sorted)

    passwords = set()
    for pwlist in all_password_lists:
        passwords.update(pwlist)

    for password in passwords:
        print(password)


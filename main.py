import os, sys, json, shutil
from multiprocessing import Pool, cpu_count
from Person import Person

def make_connections():
    os.system("python3 Create_Connections.py")

def make_filter():
    os.system("python3 Apply_Filters.py | tee wordlist_filtered.txt")

def clear_cache():
    shutil.rmtree("__pycache__", ignore_errors=True)
    shutil.rmtree("filters/__pycache__", ignore_errors=True)

def clear_profiles():
    shutil.rmtree("profiles", ignore_errors=True)
    os.makedirs("profiles", exist_ok=True)

def clear_wordlists():
    for f in os.listdir("."):
        if f.endswith(".txt"): os.remove(f)

def make_passwords():
    max_mutuals = max_time_known = 0
    for x in os.listdir('./profiles/'):
        person = Person(f'./profiles/{x}', (max_mutuals, max_time_known))
        if person.extract_mutuals_and_time_known() > (max_mutuals, max_time_known):
            max_mutuals, max_time_known = person.extract_mutuals_and_time_known()

    hierarchy = {}
    for x in os.listdir('./profiles/'):
        if x == "target.json": continue
        person = Person(f'./profiles/{x}', (max_mutuals, max_time_known))
        hierarchy[x] = person.yield_closeness()
    hierarchy_sorted = sorted(hierarchy, key=hierarchy.get, reverse=True)

    with open('profiles/target.json', 'r', encoding='utf-8') as f:
        target_data = json.load(f)

    target = [
        (target_data["first_name"], target_data["middle_name"], target_data["last_name"]),
        tuple(str(x) for x in target_data["numbers"]),
        tuple(target_data["special_characters"])
    ]

    def process_person(filename):
        from Person import Person
        from Combinator import Combinator
        person = Person(f'./profiles/{filename}', (max_mutuals, max_time_known))
        other_person = person.yield_iterables()
        target_text = set(target[0] + other_person[0])
        target_numbers = set(target[1] + other_person[1])
        target_special_characters = set(target[2] + other_person[2])
        c1 = Combinator([target_text, target_numbers, target_special_characters])
        return list(c1.return_passwords())

    with Pool(cpu_count()) as pool:
        all_password_lists = pool.map(process_person, hierarchy_sorted)

    passwords = set()
    for pwlist in all_password_lists:
        passwords.update(pwlist)

    with open("wordlist.txt", "w", encoding="utf-8") as f:
        for password in passwords:
            print(password)
            f.write(password + "\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [connections|passwords|filter|clear_cache|clear_profiles|clear_wordlists]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "connections": make_connections()
    elif cmd == "passwords": make_passwords()
    elif cmd == "filter": make_filter()
    elif cmd == "clear_cache": clear_cache()
    elif cmd == "clear_profiles": clear_profiles()
    elif cmd == "clear_wordlists": clear_wordlists()
    else:
        print("Invalid command")
        sys.exit(1)

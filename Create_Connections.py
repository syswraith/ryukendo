import os, json

os.makedirs("profiles", exist_ok=True)

def input_with_limit(prompt, min_val=None, max_val=None, no_limit=False):
    while True:
        val = input(prompt)
        if no_limit:
            try:
                return int(val)
            except ValueError:
                print("Enter a valid integer.")
        else:
            try:
                iv = int(val)
                if (min_val is not None and iv < min_val) or (max_val is not None and iv > max_val):
                    print(f"Enter an integer between {min_val} and {max_val}.")
                else:
                    return iv
            except ValueError:
                print("Enter a valid integer.")

def get_full_profile():
    return {
        "first_name": input("First name: "),
        "middle_name": input("Middle name: "),
        "last_name": input("Last name: "),
        "affiliation": [a.strip() for a in input("Affiliations (comma-separated): ").split(",") if a.strip()],
        "mutuals": input_with_limit("Mutuals (no limit): ", no_limit=True),
        "intimacy": input_with_limit("Intimacy (1-3): ", 1, 3),
        "frequency_of_contact": input_with_limit("Frequency of Contact (1-3): ", 1, 3),
        "shared_xp": input_with_limit("Shared XP (1-3): ", 1, 3),
        "time_known": input_with_limit("Time Known (no limit): ", no_limit=True),
        "numbers": [int(x) for x in input("Numbers (comma-separated): ").split(",") if x.strip()],
        "special_characters": [c.strip() for c in input("Special characters (comma-separated): ").split(",") if c.strip()]
    }

print("Enter target profile details (target.json):")
target_profile = get_full_profile()
with open("profiles/target.json", "w", encoding="utf-8") as f:
    json.dump(target_profile, f, indent=2)

n = input_with_limit("\nHow many person profiles to create? ", 1, None)
for i in range(1, n + 1):
    print(f"\nEnter details for person{i}.json")
    profile = get_full_profile()
    with open(f"profiles/person{i}.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)


import os
from Person import Person
from Combinator import Combinator


passwords = set()
hierarchy = {}
max_mutuals, max_time_known = 0,0


# maximum mutuals finder
for x in (os.listdir('./profiles/')):
    person = Person(f'./profiles/{x}',(max_mutuals, max_time_known))
    if person.extract_mutuals_and_time_known() > (max_mutuals, max_time_known):
        max_mutuals, max_time_known = person.extract_mutuals_and_time_known()


# closeness sorter
for x in (os.listdir('./profiles/')):
    person = Person(f'./profiles/{x}',(max_mutuals, max_time_known))
    hierarchy[x] = person.yield_closeness()
hierarchy_sorted = dict(sorted(hierarchy.items(), key=lambda x: x[1], reverse=True))


# generator
for x in tuple(hierarchy_sorted):
     print("The current person is", x)
     person = Person(f'./profiles/{x}', (max_mutuals, max_time_known))
     other_person = person.yield_iterables()
     target = [("Vedant", "Pravin", "Jadhav"), ("11", "04", "26"), ("%", "_", "💀")]
     
     target_text = set()
     target_numbers= set()
     target_special_characters= set()
     
     target_text.update(target[0], other_person[0])
     target_numbers.update(target[1]), other_person[1]
     target_special_characters.update(target[2], other_person[2])
     
     c1 = Combinator([target_text, target_numbers, target_special_characters])
     for x in c1.return_passwords(): passwords.add(x)

for password in list(passwords): print(password)

from Person import Person
from Combinator import Combinator


passwords = set()

for x in range(1,4):
    person = Person(f'./profiles/person{x}.json', (10, 10))
    other_person = person.yield_iterables()
    target = [("Vedant", "Pravin", "Jadhav"), ("11", "04", "26"), ("%", "_")]
    
    target_text = set()
    target_numbers= set()
    target_special_characters= set()
    
    target_text.update(target[0], other_person[0])
    target_numbers.update(target[1]), other_person[1]
    target_special_characters.update(target[2], other_person[2])
    
    c1 = Combinator([target_text, target_numbers, target_special_characters])
    for x in c1.return_passwords(): passwords.add(x)

for password in list(passwords): print(password)

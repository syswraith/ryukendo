from Person import Person
from Combinator import Combinator

person1 = Person('./profiles/person3.json', (10, 10))
other_person = person1.yield_iterables()
my_info = [("Vedant", "Pravin", "Jadhav"), ("11", "04", "26"), ("%", "_")]
my_info.extend(list(other_person))
c1 = Combinator(my_info)
for x in c1.return_passwords(): print(x)

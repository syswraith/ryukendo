from Person import Person

person1 = Person('./profiles/person3.json', (10, 10))
print(person1.yield_iterables())
print(person1.extract_mutuals_and_time_known())
print(person1.yield_closeness())

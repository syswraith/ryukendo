import json
import os
import re

class Person:

    def __init__(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
        self.text = set()
        self.special_characters = set()
        self.numbers = set()
        self.text.add(data['first_name'])
        self.text.add(data['middle_name'])
        self.text.add(data['last_name'])
        for number in data['numbers']: self.numbers.add(str(number))
        for word in data['affiliation']: self.extract_num_char(word)

    def extract_num_char(self, word):
        self.numbers.update(re.findall(r"\d+", word))
        self.special_characters.update(re.findall(r"[^a-zA-Z0-9]", word))
        self.text.add(word)

    def yield_iterables(self): return tuple(self.text), tuple(self.numbers), tuple(self.special_characters)


person1 = Person('./profiles/person3.json')
print(person1.yield_iterables())

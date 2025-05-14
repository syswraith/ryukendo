from math import sqrt
import json
import os
import re

class Person:

    def __init__(self, path, max_param):
        max_mutuals, max_time_known = max_param
        with open(path, 'r') as file:
            data = json.load(file)
        
        self.text = set()
        self.special_characters = set()
        self.numbers = set()

        self.__max_frequency = 5
        self.__max_shared_experiences = 3
        self.max_mutuals = max_mutuals
        self.max_time_known = max_time_known
        self.__max_intimacy = 3

        self.frequency_of_contact = data['frequency_of_contact']
        self.shared_experiences = data['shared_xp']
        self.mutuals = data['mutuals']
        self.time_known = data['time_known']
        self.intimacy = data['intimacy']

        self.text.add(data['first_name'])
        self.text.add(data['middle_name'])
        self.text.add(data['last_name'])
        for number in data['numbers']: self.numbers.add(str(number))
        for word in data['affiliation']: self.extract_num_char(word)

    def extract_mutuals_and_time_known(self):
        return self.mutuals, self.time_known


    def extract_num_char(self, word):
        self.numbers.update(re.findall(r"\d+", word))
        self.special_characters.update(re.findall(r"[^a-zA-Z0-9]", word))
        self.text.add(word)

    def yield_closeness(self):
        euclidean_distance = sqrt(sum([(self.__max_frequency - self.frequency_of_contact)**2, (self.__max_shared_experiences - self.shared_experiences)**2, (self.max_mutuals - self.mutuals)**2, (self.max_time_known - self.time_known)**2, (self.__max_intimacy - self.intimacy)**2]))
        closeness = (1 / (1 + euclidean_distance))
        return closeness

    def yield_iterables(self): return tuple(self.text), tuple(self.numbers), tuple(self.special_characters)


#person1 = Person('./profiles/person3.json', 10, 10)
#print(person1.yield_iterables())
#print(person1.yield_closeness())

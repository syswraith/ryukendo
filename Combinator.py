from itertools import product, permutations


class Combinator:

    def __init__(self, target):

        self.dataset = target
        self.raw_combinations = product(*self.dataset)
        self.final_passwords = set()
        
        for tup in self.dataset:
            self.final_passwords.update(tup)
        
        for combination in self.raw_combinations:
            for permutation in permutations(combination):
                self.final_passwords.add(''.join(permutation))
        
        for i in range(len(self.dataset)):
            for j in range(i + 1, len(self.dataset)):
                pair_combinations = product(self.dataset[i], self.dataset[j])
                for combination in pair_combinations:
                    self.final_passwords.add(''.join(combination))
        
        
    def return_passwords(self):
        return self.final_passwords

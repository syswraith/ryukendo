from itertools import product, permutations, combinations

class Combinator:

    def __init__(self, target):
        self.dataset = target
        self.final_passwords = set()

        # Individual elements
        for tup in self.dataset:
            self.final_passwords.update(tup)

        # Intratuple combinations
        for tup in self.dataset:
            for r in range(2, len(tup) + 1):
                for comb in combinations(tup, r):
                    for perm in permutations(comb):
                        self.final_passwords.add(''.join(perm))

        # Full Cartesian product permutations
        for combination in product(*self.dataset):
            for permutation in permutations(combination):
                self.final_passwords.add(''.join(permutation))

        # 2-tuple Cartesian products
        for i in range(len(self.dataset)):
            for j in range(i + 1, len(self.dataset)):
                for combination in product(self.dataset[i], self.dataset[j]):
                    self.final_passwords.add(''.join(combination))

        # r-tuple dataset combinations (r >= 2)
        for r in range(2, len(self.dataset) + 1):
            for selected in combinations(self.dataset, r):
                for prod in product(*selected):
                    for perm in permutations(prod):
                        self.final_passwords.add(''.join(perm))

    def return_passwords(self):
        return self.final_passwords


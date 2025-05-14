from itertools import product, permutations

#dataset = [('aryan', 'pravin', 'karekar'), ('@', '_'), ('10', '04', '06')]
#
## First, get all Cartesian products in the given order
#raw_combinations = product(*dataset)
#final_passwords = set()
#
## Add the individual elements themselves to the final password set
#for tup in dataset:
#    final_passwords.update(tup)
#
## Now permutate them and add the unique passwords
#for combination in raw_combinations:
#    for permutation in permutations(combination):
#        final_passwords.add(''.join(permutation))
#
## Generate Cartesian products for all 2-tuple combinations
#for i in range(len(dataset)):
#    for j in range(i + 1, len(dataset)):
#        pair_combinations = product(dataset[i], dataset[j])
#        for combination in pair_combinations:
#            final_passwords.add(''.join(combination))
#
## Print all final passwords
#for pw in final_passwords:
#    print(pw)
#


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

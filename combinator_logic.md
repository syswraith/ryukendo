
```python

from itertools import permutations, combinations

# first declare a tuple of elements
tup = ("a", "b", "c")

# the range of r will be from 1 to 3 [1, 3]

for r in range(1, len(tup) + 1):
    for comb in combinations(tup, r):
        print(comb)
        # (a) (b) (c) (a,b) (a,c) (b,c) (a,b,c)
        for perm in permutations(comb):
            # print(perm)
            # a b c ab ba ac ca bc cb abc ...
            print("".join(perm))

```

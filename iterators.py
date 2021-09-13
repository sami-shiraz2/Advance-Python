# Iterators
# Make counting easy

t = (1, 2, 3, 4)

for x in t:
    print(x)

print('-'*10)

## From Numpy

import numpy as np
animal = np.array(['Lion', 'Elephant', 'Cat', 'Dog'])
print(animal)

# From Iter
print('-'*10)

people = ['Sami', 'Shiraz', 'Sehraan']
i = iter(people)
print(i)
print('-'*5)
print(next(i))
print(next(i))
print(next(i))

import random

class iteration_random:
    def __init__(self) -> None:
        self.max = 5

    def __iter__(self):
        for i in range(self._max):
            yield random.randrange(0, 100)
    
    def getMax(self, val):
        self._max = val

itera = iteration_random()
itera.getMax(40)

for x in itera:
    print(x)

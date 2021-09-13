# Pickle

import pickle

def outline(func):
    def inner(*args, ** kwargs):
        print('-'*20)
        print(f'Function Name = {func.__name__}')
        func(*args, ** kwargs)
        print('-'*20)
    return inner

class Cat:
    def __init__(self, name, age, info):
        self._name = name
        self._age = age
        self._info = info

    @outline
    def display(self, msg=''):
        print(msg)
        print(f'{self._name} is {self._age} years old')
        for k,v in self._info.items():
            print(f'{k} = {v}')


mini = Cat('Mini', 20, dict(Color = 'White', Weight = 15, Loves = 'Eating'))
mini.display('From String')

## Serialize
ssc = pickle.dumps(mini)
print(ssc)

with open('Cat.txt', 'wb') as f:
    pickle.dump(mini, f)

## Deserailization
mycatt = pickle.loads(ssc)
mycatt.display('From Pickle')

with open('Cat.txt', 'rb') as f:
    disc_load = pickle.load(f)

disc_load.display('From Disc')
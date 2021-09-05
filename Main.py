## Import Cat class

import cat
from cat import Cat

## Use the class
def test():
    b = Cat('Kitkat', 1, 'Black')
    c = Cat('Mini', 4, 'White')
    print(b)
    print(c)
    print('\n')
    b.description()
    c.description()

if __name__ == "__main__":
    a = Cat('test')
    test() 


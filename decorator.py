## Decorator

## Function can be use as object
## Function pass as object and add some functionality and return it

def testDecorator(func):
    print('Before')
    func()
    print('After')

@testDecorator
def testing():
    print('Testing Func')

print('-'*10)

## Real Decorator
def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner

@makeBold
def printName():
    print('Sami Shiraz')

printName()

print('-'*10)

## Decorators with Params
def numCheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('Cannot divide with Zero')
                return False
            return True
        print(f'{o} is not an Integer')
        return False

    def inner(x, y):
        if  not checkInt(x) or not checkInt(y):
            return 
        return func(x, y)
    return inner

@numCheck
def divide(a, b):
    print(a /b)

divide(10,5)
divide(10000,5)
divide(10,'Sami')
divide(10,'cat')
divide(10,0)

## Chaining Decorators
def Outline(func):
    def inner(*arg, **kwarg):
        print('*'*20)
        func(*arg, **kwarg)
        print('*'*20)
    return inner

def Chain(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
    return inner

def OnMore(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        for x in args:
            print(f'args={x}')
        for k, v in kwargs.items():
            print(f'key={k}, value={v}')
    return inner

@Outline
@Chain
@OnMore
def Birthday(name='', age=0):
    print(f'Happy Birday {name} you are {age} Now')

@Outline
@Chain
@OnMore
def Hello(h):
    print(f'{h}')

Hello('Hello World')
Birthday(name='Sami', age=25)
## Map
## Loop without Loop
# map(fun, iteration)

people = ['Sami', 'Sehraan', 'Shiraz', 'Khan']

## Old Way
counts = []
for i in people:
    counts.append(len(i))
print(f'Old Way: {counts}')

## New Way
print(f'New Way: {list(map(len, people))}')

## More Complex
firstName = ['Sami', 'Sharif', 'Shiraz', 'Hamida']
lastName = ['Shiraz', 'Hamiya', 'WazirAli']

def merge(a, b):
    return a + ' ' + b

x = map(merge, firstName, lastName)
print(list(x))

## Combining Functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def doall(func, num):
    return func(num[0], num[1])

f = (add, sub, mul, div)
v = [[8, 10]]
n = list(v) * len(f)

m = map(doall, f, n)
print(list(m))




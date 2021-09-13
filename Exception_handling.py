
def ouline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'function name: {func.__name__}')
        func(*args, **kwargs)
        print('-'*20)
    return inner

@ouline
def divide(x, y):
    try:
        z = x / y
        print(f'Result = {z}')
    except:
        print(f'Something bad happen x = {x}, y = {y}')
    finally:
        print('Complete')

divide(2, 8)
divide(2, 'cat')
divide(2, 0)

@ouline
def test(x, y):
    try:
        assert(x>0)
        assert(y>0)
    except AssertionError:
        print(f'Failed to Assert {x}, y = {y}')
    except TypeError:
        print(f'Type Error {x}, y = {y}')
    except Exception as e:
        print(f'Something bad happen x = {x}, y = {y}, issue is {e}')
    else:
        z = x / y
        print(f'Result = {z}')
    finally:
        print('Complete')

test(2, 8)
test(2, 'cat')
test(2, 0)

class CatError:
    def __init__(self, args):
        self.args = args

## Defining a custom Exception

@ouline
def cat(qty):
    try:
        if not isinstance(qty, int):
            raise TypeError('Must be INT')
        elif qty < 9:
            raise CatError('Should not be more than 9 Cats')
        print(f'You own {qty} Cats')
    except Exception as e:
        print(f'Oops: {e.args}')
    finally:
        print('Complete')

cat(100)
cat('cat')
cat(2.7)


## Creating Class Feline
class Feline:
    def __init__(self, name):
        self.name = name
        print('Creating a Feline')

    def meow(self):
        print(f'{self.name} : Meow')

    def setName(self, name):
        print(f'{self.name} Setting name to {name}')
        self.name = name

## Creating Class Lion
class Lion(Feline):
    def roar(self):
        print(f'{self.name} : Roar')

## Creating Class Tiger
class Tiger(Feline):
    def __init__(self):
        super().__init__('No_Name')
        print('Creating a Tiger')

    def stalk(self):
        print(f'{self.name} : Stalk')

    def rename(self,name):
        super().setName(name)

c = Feline('kitty')
c.meow()
c.setName('Mini')
c.meow()

l = Lion('Lion')
l.meow()
l.roar()

t = Tiger()
t.meow()

t.rename('Tiger')
t.stalk()
    
        



class Cat:
    Name = ''
    Age = 0
    Color = ''

    def __init__(self, Name, Age=0, Color='White'):
        self.Name = Name
        self.Age = Age
        self.Color = Color
        print(f'Constructor for {self.Name}')

    def meow(self):
        print(f'{self.Name} Meow')

    def sleep(self):
        print(f'{self.Name} zzz')

    def hungry(self):
        for i in range(5):
            self.meow()

    def eat(self):
        print(f'{self.Name} nom nom nom')

    def description(self):
        print(f'Cat name is {self.Name}, She is {self.Color} Color, Her Age is {self.Age}')

    

    
    
        
    
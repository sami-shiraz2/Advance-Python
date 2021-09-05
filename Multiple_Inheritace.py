## Multiple Inheritance

## Creating Vehicle Class
class Vehicle:
    speed = 0
    def drive(self, speed):
        self.speed = speed
        print('Driving')

    def stop(self):
        self.speed = 0
        print('Stopped')

    def display(self):
        print(f'Driving speed is {self.speed} Speed')

## Creating Freezer Class
class Freezer:
    temp = 0
    def temperature(self, temp):
        self.temp = temp
        print('Freezing')

    def display(self):
        print(f'Freezing temperature is {self.temp} Temperature')

## Creating VehicleFreezer Class (Muliple Inheritance)
class VehicleFreezer(Vehicle, Freezer): ##Method Resolution Orfder
    pass

    def display(self):
        print(f'Freezer is {issubclass(VehicleFreezer, Freezer)}')
        print(f'Vehicle is {issubclass(VehicleFreezer, Vehicle)}')

        Freezer.display(self)
        print('-'*10)
        Vehicle.display(self)

t = VehicleFreezer()
t.drive(50)
t.temperature(-30)
print('-'*20)
t.display()


         

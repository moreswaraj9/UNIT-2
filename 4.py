class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Car(Vehicle):
    def move(self):
        print("Driving on the road")
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")
def show_movement(vehicle):
    vehicle.move()
car1 = Car()
bicycle1 = Bicycle()
show_movement(car1)
show_movement(bicycle1)

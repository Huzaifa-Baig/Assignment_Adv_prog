class Vehicle:
    # Class attribute

#create a class that inherits from the parent class
    def __init__(self, name, price, model,colour):
        self.colour = colour
        self.name = name
        self.price = price
        self.model = model

class Car:
   pass

car = Car("Red","Tesla", 30000, 1000)
print(car.color, car.name,  car.price,  car.model)
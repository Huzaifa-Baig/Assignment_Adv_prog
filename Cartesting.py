import unittest

class Vehicle:
    # Class attribute

    #create a class that inherits from the parent class
    def __init__(self, name, price, model, colour):
        self.colour = colour
        self.name = name
        self.price = price
        self.model = model

class TestCar(unittest.TestCase):
    def test_car_attributes(self):
        car = Vehicle("Tesla", 30000, 1000, "Red")
        self.assertEqual(car.name, "Tesla")
        self.assertEqual(car.price, 30000)
        self.assertEqual(car.model, 1000)
        self.assertEqual(car.colour, "Red")

if __name__ == '__main__':
    unittest.main()


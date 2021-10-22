import Pygame
class Cat():
    def __init__(self, name, rib, lowerback):
        self.name = name
        self.rib = rib
        self.lowerback = lowerback
    def BMI(self):
        return self.rib / ((self.lowerback /100) ** 2)
class Dog(Cat):
    def __init__(self, name, weight, height, waist,):
        super().__init__(name, weight, height)
        self.waist = waist
    def printBWH(self):
        print("waist = {}". format(self.waist))
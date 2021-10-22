import Cat
David = Cat.Cat('David', 5, 50)
print(David.name, "BMI: ", David.BMI())
Jenny = Cat.Dog("Jenny", 1, 2, 3)
print(Jenny.name, "BMI: ", Jenny.BMI())
Jenny.printBWH()
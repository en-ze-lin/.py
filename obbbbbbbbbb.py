import human
David = human.Human('David', 100, 90)
print(David.name, "BMI: ", David.BMI())
Jenny = human.Woman("Jenny", 1, 2, 3, 4, 5)
print(Jenny.name, "BMI: ", Jenny.BMI())
Jenny.printBWH()
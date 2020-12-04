class Car:

    wheels = 4

    def __init__(self):
        self.mile=22
        self.comp='MUSTANG'

c1=Car()
c2=Car()

c1.mile=30

Car.wheels=5

print(c1.mile,c1.comp,c1.wheels)
print(c2.comp, c2.mile,c2.wheels)

#outer class
class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        self.lap=self.Laptop

    def show(self):
        print(self.name,self.roll_number)

    #inner class
    class Laptop:

        def __init__(self):
            self.brand='Dell'
            self.cpu='i5'
            self.ram='8gb'

s1=Student('Atik',2)
s2=Student('Emma',3)

s1.show()
s2.show()

lap1=s1.lap
lap2=s2.lap

print(id(lap1))
print(id(lap2))

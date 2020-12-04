#I can create object of inner class inside the outer class .
#or I can create onject of inner class outside the outer class provided you see outer class name to call it.
#Now there we will create object ouside .If I don't want to create object in class Student and class Laptop.

#Because we can't access "class Laptop" beacuse it's belongs to class Student.


class Student:
    def __init__(self,name,roll_number):
        self.roll_number = roll_number
        self.name=name
        self.number=roll_number
        self.lap=self.Laptop()

    def show (self):
        print(self.name,self.roll_number)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand="Dell"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student('Atik',2)
s2=Student ('Emma',3)

s1.show()
s2.show()
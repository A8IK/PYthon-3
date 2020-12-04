class Student:
    def __init__(self, name, roll_number, laptop, cpu, ram):
        self.name=name
        self.roll_number=roll_number
        self.laptop=laptop
        self.core=cpu
        self.ram=ram


    def show(self):
        print(self.name,self.roll_number,self.laptop,self.core,self.ram)

s1=Student("Atik",2,'DELL','i5','8gb')
s2=Student("Emma",3,'Apple','i7','8gb')

s1.show()
s2.show()
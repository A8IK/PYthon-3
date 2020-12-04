class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Comnpiling")
        print("Running")


class Laptop:

#Here ide is not tyoe of string or intger for that we have to create new class as  a 'PyCharm' ...
##"ide"  is not fix with PyCharm we can change it beacuse it's a dyanmic type


    def code (self,ide):
       ide.execute()

ide=PyCharm()


lap1=Laptop()
lap1.code(ide)

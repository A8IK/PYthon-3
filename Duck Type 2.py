class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:

    def execute(self):
        print("Spelling Check")
        print("Convention Check")
        print("Compiling check")
        print("Running check")


class Laptop:

    def code(self,ide):
        ide.execute()
#We can change it to another class...
ide=MyEditor()

lap1=Laptop()
lap1.code(ide)



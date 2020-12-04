##This is a Generator Function....

def topten():

# "yield" is a special function who is converted a function to generator...
##"yield" is a generator who gives iterator..

    yield 1
    yield 2
    yield 3
    yield 4

values = topten()

print(values.__next__())
print(values.__next__())

print(values)

for i in values:
    print(i)
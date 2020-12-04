#If we use this code :
a=5
b="World"
print(a+b)
##It's not gonna be work beacause "integer" and "string" there's two different variable...

##but if we run that code :

##**Here cauttation ("") is very important otherwise it not gonna be work...(example below  code only)

a='5'
b='6'
print(a+b)

print(int.__add__(a,b))  ##This is object

##"__add__()" method is we can change as we wish if we want to do minus than we have to use "__sub__()"
##if we want to do multiplaction we have to use "__mul__()"

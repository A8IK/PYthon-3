
import sys;


i=float(input("Enter your basic salary:"))
j=float(input("Enter your ration money:"))

k=int(input("Enter your month:"))
m=float(input("Enter your medical amount:"))
z=(i+j+m) *k
print("This  is your basic income :",z)
e=float(input("Enter your eid bonus:"))
for i in range(0,1):

    if (e>0):
        print("Your eid bonus is:",e)
        continue
    elif (e<=0):
        print("     Okay,Let it go...   ")



else :
    l=float(input("Enter your boishakhi amount:"))
b=z+e+l
print("This is your total amount:",b)



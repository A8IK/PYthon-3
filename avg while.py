x1 = float(input("Enter your 1st number : "))
x2 = float(input("Enter your 2nd number : "))
x3 = float(input("Enter your 3rd number : "))
x4 = float(input("Enter your 4th number : "))
x5 = float(input("Enter your 5th number : "))
x6 = float(input("Enter your 6th number : "))
x7 = float(input("Enter your 7th number : "))
x8 = float(input("Enter your 8th number : "))
x9 = float(input("Enter your 9th number : "))
x10 = float(input("Enter your 10th number : "))

while True:
    try:

        x = (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)/10
        print("This is your average number : ",x)
        break

    except Exception as x:
        print(" 404::ERROR ")


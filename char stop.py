while True:
    try:
        x = str((input("Enter your number or character : ")))
        if(x == "."):
            break

    except Exception as x:
        print(x)

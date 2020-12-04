start = float(1.75)
stop = float(4.25)

for x in range(2,int(4.25)) : ##here I am not taking value int and float need some help and increment it 0.50

    print(x,end=" ")

    if(x<4):
        print(" ,",end=" ")

    x += .25
    print(x)
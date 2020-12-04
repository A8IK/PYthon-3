##Top ten perfect square we want to print here..ALso here we use iterator and give gnerator

def topten():

    n = 1

    while n<= 10:

##It's like return vlaue but return terminate value but it's not terminate
        sq = n*n
        yield sq
        n +=1       #iterating


values = topten()

for i in values:
    print(i)
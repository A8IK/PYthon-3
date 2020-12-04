from time import sleep  ##This sleep will alternatively print value
from threading import *

class Hello(Thread):    ##Hello is sub class of the Thread.Here we create two of one different thread
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

##Here they can run individually in different calls..

class Hi(Thread):       ##Also here 'Hi' is the subclass of the Thread.We create two of two different thread
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()  #internally it's called 'run'
sleep(0.2)    ##It'll not do collision like 'HiHello' or 'HelloHi'
t2.start()
##Creating two different Main threads here...

t1.join()
t2.join()
##Here join said hey "Bye" wait for Hello and Hi join after print bye....
print("Bye")
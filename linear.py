pos =-1  #MAINTANING POSITION [GLOBAL VARIABLE]

def search(list,n):
    i = 0       ##Here this is counter element

    while i<len(list): ##Here think about we have to go to last value  ##Here we are itereting list
        if list[i] == n:
            #print("Found Here")
            globals()['pos'] = i     #[LOCAL VARIABLE] Whenever we change local variable it's not change global variable

    ##Here 'globals' we are specificly command which globals variable we are talking about.
            return True   ##When we found the value that moment it 'return True' otherwise it 'return False'

        i = i+1         #Here incrementing value

    return False


list = [5,8,4,6,9,2]

n = 9
#n = 10

if search(list,n):
    print("Found at",pos+1)   ##'pos +1' because of it's counting like human from '1'

else:
    print("Not Found")
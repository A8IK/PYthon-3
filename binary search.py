pos = -1

def search(list,n):
    l = 0  ##[lowerbound]
    u = len(list)-1 #[Upperbound], -1 beacause it should be 1<stuff

##Here we need two condition:
#  1.'lowerbound' is always small than upperbound.
#  2. The moment we found the value
    while 1<= u:
        mid = (l+u) // 2   #[finding mid]. We want here integer division not a normal division
                            ##'//' will give me into the division

        if list[mid] == n:  ##We are comparing value with what i am searching for
            globals()['pos'] = mid
            return True

        else:  ##Here we are changing upper and lower bound if didn't match with what i am looking for
            if list[mid]<n:
                l = mid+1

            else:
                u = mid-1   ##Skip mid value here

    return False        ##Give one spce for more if "Not Found" you found

list = [4,7,8,12,45,99,102,702,1097]
n = 1097

if search(list, n):   ##Here we are passing list and n
    print("Found at",pos+1)

else:
    print("Not Found")
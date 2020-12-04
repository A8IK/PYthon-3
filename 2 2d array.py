from numpy import*
arr1=array([
    [1,2,5,6,10,12],
    [4,6,9,8,20,19]
  ])
arr2=arr1.flatten()
arr3=arr2.reshape(2,2,3)
print(arr3)
print('This program shows how arguements work for mutable objects')

def changer(a,b):       #This shows how mutable object such as lists an dictionaries behave
    a=2
    b[0]='spam'

X=1
L=[1,2]
changer(X,L)
print(X,L)

#Above it is clear to see that X will remain the same as a is local 
#However as the list passed to the function is mutable 
#When b[0] is changed it will also change the value when L[0] is called
#This is because L and b reference the same object but unlike the integer case
#lists are mutable meaning the object itself can be changed
#As in the integer case the object can't be changed a new object is created
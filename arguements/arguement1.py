print('This program shows how arguements work')

def f(a):       #This wont effect the variable b as a lives inside the function
    print(a)    
    a=99
    print(a,b)

b=88
f(b)
print(b)

#The point of this program is to show how a and b are connected 
#a only shares the same object reference as b when initally in the function
#as soon as a is changed, a new object is created 
#This is similar to copying a variable into the function
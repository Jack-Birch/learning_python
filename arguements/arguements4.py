#Gonna be looking at returning values from functions 
#This is easy to do in python due to its polymorphism 

def func(a):
    a=a+1
    L=[a,a]
    return L 

Y=4
X=[1,2]
X=func(Y)
print(X)


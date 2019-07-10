#In order to make a copy of a list to a function look below

def changer(a,b):
    a=2
    b[0]='spam'

X=1
L=[1,2]
changer(X, L[:])        #The L[:] statement send a copy of the L list to the function 
print(X,L)              #L will be unchanged when this program is run

#Another alternative is to put a b=b[:] inside the function 
#This means that b will be working on a copy of itself 
#The orignial list passed to the function L wont be effected
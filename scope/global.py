#The process of using global variables in a piece of code

#In this set of statements the variable X is re-assigned in the function 
#but as X in the function is local to the function, it wont effect what 
#is outside it 

X=88 

def func():
	X=99
	
func()
print(X)


#In this set of statments the variable X is re-assigned in the function 
#using the global command 

X=88
def func1():
	global X		#Adding the global command uses the global X in the function
	X=99

func1()
print(X)

#If there is 2 functions, one enclosing another, the command 'non local'
#will make any changes to the variable in the lower function prominent in 
#the top part of the function
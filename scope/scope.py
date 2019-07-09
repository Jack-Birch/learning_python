#GLOBAL SCOPE

X=99			#X and func assigned in module: global 

def func(Y):		#Y and Z assigned in function: locals 
	#local scope
	Z=X+Y		#X is global 
	return Z

print(func(1))			#Func in a module: result=100 

#This gives information on how scopes work with X being a global variable
#Y and Z are the local variables as they only live while the function runs
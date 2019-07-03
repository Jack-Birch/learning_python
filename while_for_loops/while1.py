x=10
while x:			#This means while x is not empty 
	x=x-1
	if x%2!=0:
		continue	#The continue statment takes you to the top of the loop 
	print(x,end='')		#This avoids the line break after printing
				#The end statment replaces the line break

x=10 				#This statement below is much simpler than the one above
while x:			#Dont always need to use a continue statment 
	x=x-1
	if x%2==0:
		print(x,end='') 	

x=5 				#Testing my knowledge of if statments in python 
while x==5:
	if x==5:
		print(x,end=' ')
		x=x-1
	elif x==4:
		print(x,end=' ')
		x=x-1
	else:
		print(x,'poo', end=' ')
		x=x-1
else:						#Can add an else statment to the end of the while loop
	print('I skipped the while loop')
		
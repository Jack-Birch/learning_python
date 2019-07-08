#This piece of code runs two procedures, to show how variables and objects are assigned in python

L1=[1,2,3]
L2=L1
print('The value in L1 is:',L1)		#L1 and L2 are assigned the same reference
print('The value in L2 is:',L2)
L1[0]=24				#As the object is mutable the first element changes 
print('The value in L1 is:',L1)		#Hence when printed, as L1 and L2 point to the same object 
print('The value in L2 is:',L2)		#The first element of L2 will have changed as well 

print('~ The next procedure ~')

L1=[1,2,3]
L2=L1[:]				#This copies the list of L1 so that L1 and L2 reference to different objects
print('The value in L1 is:',L1)
print('The value in L2 is:',L2)
L1[0]=24				
print('The value in L1 is:',L1)		#Therefore L1 is changed but L2 remains the same 	 
print('The value in L2 is:',L2)
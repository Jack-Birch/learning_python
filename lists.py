L=['hi','this','is','a','list',123]		#How to declare a list
print(len(L))					#The length of a list
L.append('NI')					#How to add to a list
L.pop(5)					#Deletes the sixth element of the list (as it starts from 0)
print(L)

B=['bb','cc','aa']
print(B)
B.sort()					#Sorts the list in to alphabetical order
print(B)
B.reverse() 					#Sorts the list into reverse alphabetical order
print(B)

M=[[1,2,3],[4,5,6],[7,8,9]]			#Python can also store a matrix of numbers 
print(M)
print(M[1][2])					#Print the second row third column M[row][column]
print(M[0])					#Will only print the first row

col2=[row[1] for row in M]			#Will grab the second column in M
print(col2)	

print('This is to test the string data type:''%s'%(B[0])) 	#Testing that string data type works
print('B contains: %s %s %s' %(B[0],B[1],B[2]))			#Variables can be placed using placeholders
								#This is a more safe way to program 				
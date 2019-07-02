f=open('data.txt','w') 		#This creates and opens a file called data.txt 
f.write('Hello World\n')
f.write('I am writing to a file using python')
f.close()			#The close file doesnt accept an arguement 

f=open('data.txt','r')		#Open the file for reading
text=f.read()			#File contents is stored to text
print(text)
print(text.split())		#Text is stored as a string 			
f.close()
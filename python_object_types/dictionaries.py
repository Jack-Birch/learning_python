D={'food':'sausage','quantity':4, 'colour':'pink'}	#Associate a set of values with a key 
print(D['food']) 					#Will return the word associated with food

D={}						#This creates a dictionary 
D['Name']='Stephen'				#Dictionaries in general can be good for coding a search 
D['Job']='Builder'
D['Age']=22
print(D)	

C={}						#Can nest things in dictionaries 
C['Name']={'first':'Bob','second':'Smith'} 
C['Job']=['Builder','Personal Trainer']
C['Age']=22
print(C)

print("%s %s %s" %(C['Name']['first'],C['Name']['second'],C['Age'])) 	#still using placeholders 

C['Job'].append('Footballer') 			#Can expand the list nested in the dictionary 
print(C)
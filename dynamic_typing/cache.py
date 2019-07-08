X=2			#Have two variable assigned to two different objects 
Y=2
print(X==Y)
print(X is Y)

#We expect second one to be false 
#It will actually be true as python stores small values in the cache
#So both variables will point to the one object in the cache
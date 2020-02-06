print("Hello this is my python program ", end='')
x="String"
print(x)

x=10 
x=x*10
print(x*10)

x=['a','b','c']
for i in range(3):
    print(i,end='')
    x.append(i)

print ('This is my new list')
s=0
while s!=6:
    print(x[s], end='')
    s=s+1

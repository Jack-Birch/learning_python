import matplotlib.pyplot as plt 

x=[1,2,3,4,5,6]
y=[2,3,1,5,2,6]	
#data points for my graph 

plt.plot(x, y, color='green', linestyle='dashed', linewidth =2, marker='o', markerfacecolor='blue', markersize=12)
#Above are ways to customise a graph in python

plt.ylim(1,8)
plt.xlim(1,8)
#setting y and x axis range

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Some cool customizations!')
plt.show()
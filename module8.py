#Playing with the copy function
x=[[1,2,3],[4,5]]
import copy
y= copy.copy(x)
z= copy.copy(x)
y[0][1]=6
z[1] = 6
print("This is testing and experimenting with the copy function.")
print(y)
print(x)
print(z)
print("")

#Using the data set I made before for itertools operations
#Part one: using intertools.cycle
print("Testing intertools.cycle:")
import itertools
counter = 0
for i in itertools.cycle(x):
	print(i),
	counter = counter+1
	if counter>5:
		break
print("")

#Part two: using itertools.repeat
print("Testing intertools.repeat:")
import itertools
print(list(itertools.repeat(x,3)))
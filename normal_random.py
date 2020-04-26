import numpy.random as rand
fhand = open("normal",'w')
for j in range(100000000):
	fhand.write(str(rand.random())+"\n")
print("Finished")

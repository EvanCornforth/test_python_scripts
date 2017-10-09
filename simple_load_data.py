#Written by Evan Cornforth

import numpy as np

mydata = np.loadtxt(fname = 'some_data.csv', delimiter = ',')

print mydata

f = open ('some_data.csv', 'r')

lines = f.readlines()

for x in lines:
	print x

line = [lines[i].split(',') for i in range(3)] 

for i in range(3):
	for j in range(4):
		print line[i][j]

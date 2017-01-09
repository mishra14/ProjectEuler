max = 4000000
i = 1
j = 2
res = j

while(j < max):
	i, j = j, i+j
	if(j%2 == 0):
		res = res + j
	
print "Answer: {}".format(res)

with open("files/input_p8.txt") as f:
    str = f.readline()

max_product = 0L

for i in xrange(len(str)-12):
	product = 1L
	for j in xrange(i, i+13):
		product = product * int(str[j])
		if(product == 0):
			break
		if(product > max_product):
			max_product = product

print "Answer: {}".format(max_product)
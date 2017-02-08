import string

with open("files/p022_names.txt") as f:
	content = f.readlines()[0].replace("\"", "").split(",")
	
sorted_names = sorted([l.strip() for l in content])

sum = 0L
i = 0

for name in sorted_names:
	i += 1
	word_sum = 0L
	for ch in name:
		word_sum += string.uppercase.index(ch) + 1
	sum += (word_sum * i)
		
print "Answer: {}".format(sum)


lnum = [23,54,645,56,7,534,657,45]
lnew = []

def find_lowest(numlist):
	lowest = lnum[0]
	for x in lnum:
		if (x < lowest):
			lowest = x
	return lowest

while (len(lnum) > 0):
	x = find_lowest(lnum)
	lnew.append(x)
	lnum.remove(x)
print lnew

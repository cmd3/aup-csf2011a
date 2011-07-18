lnum = [23, 35, 35, 654, 46, 345]
lnew = []

def randomize(randomlist):
	random = lnum[0]
	for x in lnum:
		if (x % 2 == 0):
			random = x
	return random
	
while len(lnum) != 0:
	x = randomize(lnum)
	lnum.remove(x)
	lnew.append(x)
	
print (lnew)


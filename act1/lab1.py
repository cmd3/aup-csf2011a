lnum = [4563, 45, 2345, 456, 453]
lnew = []
def inverse(numlist):
	inverse = lnum[0]	
	for x in lnum:
		if (x != inverse):
			inverse = x
	return inverse
while (len(lnum) > 0):
	x = inverse(lnum)
	lnew.append(x)
	lnum.remove(x)
print lnew 


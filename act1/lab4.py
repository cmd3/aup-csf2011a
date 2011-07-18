lnum = [3245, 3245, 256, 3476, 3423, 2356]
summy = 0.00
for x in lnum:
	y = lnum[0]
	if x >= y:
		summy = summy + x
	elif x <= y:
		summy = summy + x
average = summy / len(lnum)
print average

x = random(3)
loop = 0
print"Let's play game"
print"Can you guess my number(1-1000)?"
y = int(raw_input(How many trials did you want?  ))

guess = int(raw_input(Enter the number : ))

while (loop != y):

	if (guess < x):
		print"Lower!"
	elif (guess > x):
		print"Higher!"
	else:
		print"You Got it!"

print"Game Over!"
		


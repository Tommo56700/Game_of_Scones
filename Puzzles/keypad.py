def puzzle_keypad():
	import random 
	number = random.randrange (0,9) #random correct number in the range of 0-9 
	health = 100 #edit this to match game health variable name
	print ("You've encountered a keypad,")# edit this to cahnge introudction of puzzle 
	print ("You've already guessed the first three numbers from the keypad as flour was still on the keys")
	print ("Now you must now guess the last digit")

	temp= int(input())
	while temp != number:
		if temp> number: 
			print ("The number may be smaller")
			health = health - 10
			print ("You have been shocked by the keypad. You lost 10 health, and you have ",  health, "remaining")
			temp= int(input("Guess again: "))
		else: 
			print("The last number may be higher")
			health = health - 10
			print ("You have been shocked by the keypad. You lost 10 health, and you have ",  health, "remaining")
			temp= int(input("Guess again: "))
	print("You have correctly guessed the numberpad code") #Discription for completing the puzzle 
	return health
#Text validation still needs to be implemented into the puzzle, for example, only allowing digits
# runs the above function
puzzle_keypad()
def word_search():

	print("You are stuck at a door. This door requires a keyword to open the door")
	print("You notice on the wall next to the door is a cluster of random letters written in flour,")
	print("from this you must figure out the key word to open the door")# Discription of the puzzle 
	print("The wall reads:")
	print(" S A B M A Y R")
	print(" Z C A R T Y A") ### Here is the wordsearch 
	print(" R R O C K O N")
	print(" Y Y X N K L N")
	print(" L A M C E P O")

	entry = str(input("")) 
	while entry != "SCONE": # loops until SCONE is entered. 
		if entry == "hint": #Game also offers a hint
			print ("You think to yourself... the keyword must be delicious!")
			entry = str(input(""))
		else:
			print ("Try again, this is the incorrect password")
			entry = str(input("Guess again"))
	print ("This is the correct keyword. The door ahead opens rapidly!") # Discription upon completion
### feel free to edit this code and change the text to better match the story
word_search()
print("") ### Input the intro the puzzle here !!!
longstring = """

()    ()      ()      ()     ()   ()()()()   ()      ()        ()      ()    ()
()    ()     ()()     ()()   ()  ()          ()()  ()()       ()()     ()()  ()
()    ()    ()	()    ()  () () ()          ()  ()()  ()     ()  ()    () () ()
()()()()   ()()()()   ()   ()() ()  ()()()  ()  ()()  ()    ()()()()   ()  ()()
()    ()  ()	  ()  ()    ()) ()      () ()    ()    ()  ()      ()  ()   ())
()    () ()        () ()     ()	()()()()  ())    ()    () ()	    () ()    ()

				     ___________
				    /          |
				   |           |
				   |          (_)
				   |          \|/
				   |           |
				   |          / \\
				   |_______

"""
print(longstring)

answer = list("PYTHON") #Correct answer for hangman
answer_coppy = list("PYTHON")
word = list(len(answer_coppy) * "-")
incorrect_letters = "" #Holds list of incorrect letters
fails = 0 #counts fails
used_letters = ""

while answer:
	print("Word: ", "".join(word))
	print("You have used:", list(used_letters))
	while True:
		entry = (input("Enter your guess! ")).upper()
		if len(entry) != 1 or not entry.isalpha():
			print("Please enter a single character.")
		else:
			break

	used_letters += entry
	

	if entry in answer:
		print(entry + " is correct!\n")
		answer.remove(entry)
		word[answer_coppy.index(entry)] = entry

	else:
		fails = fails + 1 #adds 1 to fail
		incorrect_letters += entry #adds the incorrect letter to the incorrect_letters

		if fails == 1: # depending upon the amount of fails will depend on the image displayed
			longstring = """ 




			______
			""" ### printed the above hangman state
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters) # prints the inccorrect letters entered so far

		elif fails == 2:
			longstring ="""


				    /          
				   |         
				   |         
				   |        
				   |         
				   |         
				   |______
			"""
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)

		elif fails == 3:
			longstring ="""

				     ___________
				    /     
				   |         
				   |         
				   |         
				   |         
				   |         
				   |______
				   """
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)

		elif fails == 4:
			longstring ="""
				     ___________
				    /          |
				   |           |
				   |         
				   |         
				   |        
				   |         
				   |______
				   """
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)

		elif fails == 5:
			longstring ="""
				     ___________
				    /          |
				   |           |
				   |          (_)
				   |          
				   |          
				   |          
				   |______
				   """ 
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)

		elif fails == 6: 
			longstring ="""

				     ___________
				    /          |
				   |           |
				   |          (_)
				   |          \|/
				   |           
				   |          
				   |______
			"""
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)

		elif fails == 7: 
			longstring ="""

				     ___________
				    /          |
				   |           |
				   |          (_)
				   |          \|/
				   |           |
				   |          
				   |______
				   """
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)

		else: 
			longstring ="""

				     ___________
				    /          |
				   |           |
				   |          (_)
				   |          \|/
				   |           |
				   |          / \\
				   |_______
				   """ 
			print (longstring)
			print ("GAME OVER!!!")
			quit() 

print ("PYTHON is the correcet answer!") ### edit to match game! finaly text upon completion of puzzle


### May be worth adding loss of health if you fail to complete hangman. In its current state hangman does not effect the payer in any way/. 
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
				   |_____

Please use all caps to answer

"""
print (longstring)
answer = "PYTHON" #Correct answer for hangman
fl = "P" #Defiing each letter
sl = "Y"
tl = "T"
fol= "H"
fil= "O"
sil= "N"
incorrect_letters= "" #Holds list of incorrect letters
fails = 0 #counts fails 
answer = 6 # answer is 6
current= 0 # current correct inputs
used_letters= ""

while current < 6: # loop if less than 6. When current is 6 you have won
	entry = input("Enter your first guess!")
	used_letters = str(used_letters) + str(entry)

	if entry == fl or entry == sl or entry == tl or entry == fol or entry == fil or entry == sil: #if any of these, then +1 to current
		current = current + 1 
	else:
		fails = fails + 1 #adds 1 to fail

		if fails == 1: # depending upon the amount of fails will depend on the image displayed
			incorrect_letters = entry + ", " + incorrect_letters #adds the incorrect letter to the incorrect_letters
			longstring = """ 




			_____
			""" ### printed the above hangman state
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters) # prints the inccorrect letters entered so far
		elif fails == 2:
			incorrect_letters = entry+ ", " + incorrect_letters 
			longstring ="""


				    /          
				   |         
				   |         
				   |        
				   |         
				   |         
				   |_____
			"""
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)
		elif fails == 3:
			incorrect_letters = entry + ", " + incorrect_letters 
			longstring ="""

				     ___________
				    /     
				   |         
				   |         
				   |         
				   |         
				   |         
				   |_____
				   """
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)
		elif fails == 4:
			incorrect_letters = entry + ", " + incorrect_letters 
			longstring ="""
				     ___________
				    /          |
				   |           |
				   |         
				   |         
				   |        
				   |         
				   |_____
				   """
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)
		elif fails == 5:
			incorrect_letters = entry + ", " + incorrect_letters 
			longstring ="""
				     ___________
				    /          |
				   |           |
				   |          (_)
				   |          
				   |          
				   |          
				   |_____
				   """ 
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)
		elif fails == 6: 
			incorrect_letters = entry + ", " + incorrect_letters 
			longstring ="""

				     ___________
				    /          |
				   |           |
				   |          (_)
				   |          \|/
				   |           
				   |          
				   |_____
			"""
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)
		elif fails == 7: 
			incorrect_letters = entry + ", " + incorrect_letters 
			longstring ="""

				     ___________
				    /          |
				   |           |
				   |          (_)
				   |          \|/
				   |           |
				   |          
				   |_____
				   """
			print (longstring)
			print ("Incorrect Letters: " + incorrect_letters)
		else: 
			incorrect_letters = entry + ", " + incorrect_letters 
			longstring ="""

				     ___________
				    /          |
				   |           |
				   |          (_)
				   |          \|/
				   |           |
				   |          / \\
				   |______
				   """ 
			print (longstring)
			print ("GAME OVER!!!")
			quit() 

print ("PYTHON is the correcet answer!") ### edit to match game! finaly text upon completion of puzzle


### May be worth adding loss of health if you fail to complete hangman. In its current state hangman does not effect the payer in any way/. 
import time
import random
import os
import sys

#note these dictionaries should probably be in their own files and only serve as a rough template for finalised versions. I really suck with dictionaries...

enemy = {
    "name":"Johnson",
    "intro": "The room contains an enemy. They prepare to attack",
    "strength":5,
    "health":20,
    "dexterity":0,
    "speed":5,
    "weakness" : "hammer",
    "items" : "key",
    }


player = {
    "name":"Howard",
    "health":2,
    "speed":1,
    "strength":1,
    "dexterity":5,
    }



equiped = "hammer"            #this should contain to a weapon/item the player selects from their inventory outside of combat.


inventory = ["hammer"]          #this should contain a list of all items the player has picked up



#################################################################################################################################################


def character_creation():   #this function should be run at the start of the game to assign stats to the player

    attributes_left = 4

    player["name"] = input("Please enter your name: ")

    print ("You may now assign your 4 core attributes. Remember your attributes cannot be greater than 10.")
    time.sleep(0.5)

    while attributes_left ==4:
        stats_remaining = 24
        attributes_left = 4
        print ("ATTRIBUTE POINTS REMAINING: " + str(stats_remaining))
        print ("Strength affects how much damage your attacks will cause.")
        player_input = int(input("Please enter your strength: "))
           
        if (player_input <=10) and (player_input <= stats_remaining) and (player_input > 0) and (attributes_left == 4):
            player["strength"] = player_input
            attributes_left = 3
            stats_remaining = stats_remaining - player_input
            time.sleep(0.5)
        else:
            print("Invalid Strength. Please select a valid allocation of points.")

        while attributes_left ==3:
            print ("ATTRIBUTE POINTS REMAINING: " + str(stats_remaining))
            print("Dexterity affects how likely your attacks are to hit.")
            player_input = int(input("Please enter your dexterity: "))
            time.sleep(0.5)
            
            if (player_input <=10) and (player_input <= stats_remaining) and (player_input > 0) and (attributes_left == 3):
                player["dexterity"] = player_input
                attributes_left = 2
                stats_remaining = stats_remaining - player_input
                time.sleep(0.5)
            else:
                print("Invalid Dexterity. Please select a valid allocation of points.")
                
            while attributes_left ==2:  
                print ("ATTRIBUTE POINTS REMAINING: " + str(stats_remaining))
                print ("Speed affects how easy it is to retreat or dodge enemy attacks.")
                player_input = int(input("Please enter your speed: "))
                time.sleep(0.5)
   
                if (player_input <=10) and (player_input <= stats_remaining) and (player_input > 0) and (attributes_left == 2):
                    player["speed"] = player_input
                    attributes_left = 1
                    stats_remaining = stats_remaining - player_input
                else:
                    print("Invalid Speed. Please select a valid allocation of points.")

                while attributes_left ==1:
                    print ("ATTRIBUTE POINTS REMAINING: " + str(stats_remaining))
                    print ("Endurance affects how much damage you can take before dieing.")
                    player_input = int(input("Please enter your endurance: "))
                    time.sleep(0.5)

                    if (player_input <=10) and (player_input <= stats_remaining) and (player_input > 0) and (attributes_left == 1):
                        player["health"] = player_input*10
                        stats_remaining = stats_remaining - player_input
                        attributes_left =0

                    else:
                        print("Invalid Endurance. Please select a valid allocation of points.")
                


        if not(stats_remaining == 0) and (attributes_left == 0):
            if input("You aren't using all your attribute points. Would you like to reallocate your attributes?").lower() == "yes":
                attributes_left = 4
                stats_remaining = 24
            

#################################################################################################################################################

                          
def player_attack(player_strength, player_dexterity, enemy_speed, enemy_weakness, enemy_name):  #if the player attacks          
    hit_chance = ((player_dexterity-enemy_speed)*10) + (random.random()*0.75*100)                            #calculate chance for player to hit

    if (hit_chance >= 50) and (equiped == enemy_weakness):                                             #if player hits and is using weapon enemy weak to.
        player_attack = int(round(player_strength * 2 * +3*random.uniform(0.8,1.2)))                       #calculate damage done by player. Base strength multiplied by 2 due to enemy_weakness, +-20%
        enemy["health"] = enemy["health"]-player_attack                                       #inflict damage
            
        print("You attack " + enemy_name + " for " + str(player_attack) + " points of damage.")                   #inform player of damage dealt
        time.sleep(2)
        print(enemy_name + " has " + str(enemy["health"]) + " hitpoints remaining.")

    elif hit_chance >=50:                                                                               #if player hits
        player_attack = player_strength * +3*random.uniform(0.8,1.2)                                                  #calculate damage done by player. Base strength, +-20%
        enemy["health"] = enemy["health"]-player_attack                                       #inflict damage
            
        print("You attack " + enemy_name + " for " + str(player_attack) + " points of damage.")                   #inform player of damage dealt
        time.sleep(2)
        print(enemy_name + " has " + str(enemy["health"]) + " hitpoints remaining.")
        
    else:
        print("You missed!")
        time.sleep(1)


#################################################################################################################################################
        
def evacuate(player_speed, enemy_speed):                                           #if player tries to retreat
    retreat = False
    
    if player_speed > (enemy_speed+1):                                                        #if player is 2 points faster, they escape
        retreat = True
        print("You easily get away")
        return (retreat)

    elif (player_speed+1) < enemy_speed:                                                      #if player is 2 points slower, they cant escape and end the turn.
        print ("You can't shake 'em!")
        return (retreat)
    else:
        retreat_chance = random.random()                                                    #otherwise they have a 50/50 chance to escape
                          
        if retreat_chance > 0.5:
            retreat = True
            print("You just barely get away!")
            return (retreat)              
        else:
            print ("You almost get away...")
            retreat = False
            return (retreat)

#################################################################################################################################################


                    
def enemy_attack(player_speed, enemy_dexterity, enemy_strength):                           #During an enemy turn
    hit_chance = ((enemy_dexterity-player_speed)*10) + (random.random()*100)                    #calculate chance for enemy to hit
                              
    if hit_chance >=50:
        enemy_attack = int(round(enemy_strength*random.uniform(0.8,1.2)))
        player["health"] = player["health"] - enemy_attack                                            #If then enemy hits the player. Damage = to enemystrength value +-20%
                  
        print(enemy["name"] + " attacks you for " + str(enemy_attack) + " points of damage.")            #inform player of damage dealt
        time.sleep(2)
        print("You have " + str(player["health"]) + " hitpoints remaining.")
                          
    else:
        print(enemy["name"] + " attacked you, but missed")                                         #inform the player they got lucky and increment the turn

#################################################################################################################################################


def victory(enemy_name):                                                                            #This function should be run in the event the player defeats an enemy.
    print ("YOU DEFEATED " + enemy_name + ".\n YOU RECIEVED: " +enemy["items"])
    inventory.append(enemy["items"])                                                                     #player recieves reward for defeating the enemy


#################################################################################################################################################


def defeat():                                                                               #This function should be run in the event the player dies
    print("YOU DIED. THE HOLY SCONE WILL NEVER BE FINISHED. THE WORLD WILL END.")
    time.sleep(2)
    player_input = input("Would you like to restart? (y/n)")
    if player_input.lower() == ("y"):
        os.execl(sys.executable, sys.executable, * sys.argv)                                    #restarts the program
    elif player_input.lower() == ("n"):
        exit()


#################################################################################################################################################


def take(item_id):                                   #this function was my part of my solution for template 2. Likely needs to be adjusted for new room values
    item_present = False
    
    for item in current_room["items"]:
        if (item_id==item["id"]):
            item_present = True
            current_room["items"].remove(item)
            inventory.append(item)
    if item_present == False:
        print("You can't take that.")


#################################################################################################################################################


def show_stats():                                   #this function is simply used to display the players stats as a reminder
    print (player["name"].upper())
    time.sleep(1)
    print ("HITPOINTS: " + player["health"] + "/100")
    print ("STRENGTH: " + player["strength"])
    print ("DEXTERITY: " + player["dexterity"])
    print ("SPEED: " + player["speed"])

    
#################################################################################################################################################


def show_inv():                                     #this function is used to display the players inventory as well as their equiped weapon/item
    index = 0
    print ("You are carrying: ")
    for index in len(inventory()):
        print ("- " + inventory(index))
    print ("You currently have equiped: " + equiped())


#################################################################################################################################################


def combat(enemy):               #this code currently serves as a basic framework for what I think should be possible with the combat system. However I can't really go too deep without seeing what else is going on in the program.

    print(enemy["intro"])
    
    turn = 0                #Initialise setup variables. Ensure turn and player_turn are reset.
    player_turn = False
    retreat = False                  
    
    while ((player["health"] > 0) and (enemy["health"] > 0) and (retreat == False)):                     #Until someone dies or retreats, repeat
        time.sleep(1)
        
        if (turn == 0 and player["speed"] > enemy["speed"]) or (player_turn == True):                             #if players turn
            player_input = input("What do you want to do?\n")
                       
            if player_input == "attack":                                                                        #if player tries to attack
                player_attack(player["strength"], player["dexterity"], enemy["speed"], enemy["weakness"], enemy["name"])
                turn= turn+1
                player_turn = False
      
            elif player_input == ("retreat" or "run away" or "run"):                                            #if player tries to run
                retreat = evacuate(player["speed"], enemy["speed"])
                turn= turn+1
                player_turn = False
            
            elif player_input == ("equip" + player_input(1)) and (len(player_input)>1) and (player_input(1,"",1) in inventory):     #if player tries to equip item from their inventory
                equiped = player_input(1,"",1)
                turn= turn+1
                player_turn = False

            else:
                print("You can't do that.")

        else:                                                                                           #if enemies turn
            enemy_attack( player["speed"], enemy["dexterity"], enemy["strength"])
            player_turn = True

    if player["health"] > 0 and retreat == False:                                   #This code handles what happens to the player after the encounter based on if they won, lost or ran.
            victory(enemy["name"])
    elif player["health"] <= 0:
            defeat()


#################################################################################################################################################

combat(enemy)
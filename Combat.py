from player import *
from enemy import *
import time

#note these dictionaries should probably be in their own files and only serve as a rough template for finalised versions. I really suck with dictionaries...

enemy = {
    ["name"] =
    ["strength"] =
    ["health"] =
    ["speed"] =
    ["exp_gain"]=
    ["items"] =
    }


player = {
    ["health"] = 
    ["speed"] =
    ["strength"] =
    ["exp"]
    }

equiped = {             #this should link to a weapon/item the player selects from their inventory outside of combat.
    ["name"] =
    }

inventory = {}






def combat(enemy_name):               #this code currently serves as a basic framework for what I think should be possible with the combat system. However I can't really go too deep without seeing what else is going on in the program.
    
    turn = 0                #Initialise setup variables. Ensure turn and player_turn are reset.
    player_turn = False

    player_strength = player["strength"]        #Assign values to player/enemy stats for combat.
    player_health = player["health"]
    player_speed = player["speed"]
    weapon_multiplier = equiped[name["multiplier"]]
    enemy_name = enemy["name"]
    enemy_strength = enemy["name"["strength"]]
    enemy_health = enemy["name"["health"]]
    enemy_speed = enemy["name"["speed"]]
    
    while (player_health > 0) or (enemy_health > 0) or (retreat = True):                            #until someone dies or retreats, repeat
        player_input = input("What do you want to do?") 
            if (turn == 0 and player_speed > enemy_speed) or (player_turn == True):                     #determine who attacks first
                if player_input = "attack":
                    player_attack = strength * weapon_multiplier * random.uniform(0.8,1.2)                  #calculate damage done by player. Base strength multiplied by weapon modifier +-20%
                    enemy_health = enemy_health-player_attack                                               #inflict damage
                    player_turn = False                                                                     #forces next turn to be enemy attack
                    turn = turn+1                                                                           #increment turn counter
            
                    print("You attack " + enemy_name + " for " + player_attack + " points of damage.")       #inform player of damage dealt
                    time.sleep(2)
                    print(enemy_name + " has " + enemy_health + " hitpoints remaining.")
                          
                elif player_input = ("retreat" or "run away" or "run"):                                     #if player tries to run
                          
                    if player_speed > enemy_speed+1:                                                        #if player is 2 points faster, they escape
                        retreat = true
                        print("You easily get away")
                    elif player_speed+1 < enemy_speed:                                                      #if player is 2 points slower, they cant escape and miss a turn.
                        print "You can't shake 'em! You lose your chance to hit first."
                        turn = turn+1
                    else:
                        retreat_chance = random.random()                                                    #otherwise they have a 50/50 chance to escape
                        if retreat_chance > 0.5:
                            retreat = true
                            print("You just barely get away!")
                        else:
                            print ("You almost got away. Keep trying!")
                            turn = turn+1
            else:
                enemy_attack = enemy_strength*random.uniform(0.8,1.2)
                player_health = player_health - enemy_attack                                            #If it's enemies turn enemy hits player. Damage = to enemystrength value +-20%
                player_turn = True                                                                      #force next turn to be player attack
                turn = turn+1                                                                           #increment turn counter
                  
                print(enemy_name + " attacks you for " + enemy_attack + " points of damage.")            #inform player of damage dealt
                time.sleep(2)
                print("You have " + player_health + " hitpoints remaining.")

    if player_health > 0 and retreat = False:                   #This code handles what happens to the player after the encounter based on if they won, lost or ran.
        victory(enemy["name"])
    elif player_health <= 0:
        defeat()



def victory (enemy_name):   #This function should be run in the event the player defeats an enemy.
    print ("YOU DEFEATED " + enemy_name + ".\n YOU GAINED " + enemy["exp_gain"] + "EXP.\n YOU RECIEVED: " enemy["item"])
    inventory.append(enemy["item"])
    player["exp"] = player["exp"] + enemy["exp_gain"] * random.uniform(0.8,1.2)




def defeat:         #This function should be run in the event the player dies
    print("YOU DIED. THE HOLY SCONE WILL NEVER BE FINISHED. THE WORLD WILL NOW END.")
    time.sleep(2)
    player_input = input("Would you like to restart? y/n")
    if player_input = ("y" or "Y")
        #restart program
    elif player_input = ("n" or "N")
        exit()

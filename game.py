#!/usr/bin/python3

import random
import time

from map import rooms, puzzle_rooms, boss_rooms
from maze import maze_rooms
from bosses import bosses

from player import *
from items import *
from gameparser import *
#from colorama import Fore, Back, Style

game_stage = 0

def opening():
    """This function prints all of the opening text for the game.
    """
    #input(Fore.YELLOW + Style.BRIGHT + "\nWelcome!\n" + Style.NORMAL)
    print("\nWelcome!\n")
    #time.sleep(1)
    print("In a world where baking is the only form of solice, one chef strives to be the best, like no one ever was!")
    #time.sleep(2)
    print("Only one obsticle stands in your way,")
    #time.sleep(2)
    print("Mary Berry and her tyranical rule over the seven kingdoms!")
    #time.sleep(2)
    print("For too long has this evil overlord of the croissant reigned down on all other noble patissiers.")
    #time.sleep(2)
    print("Cursed by an evil spell placed on them, all baking endeavours attempted by anyone other than Mary Berry will ")
    #time.sleep(2)
    print("burn, fall flat or just fail miserably.")
    #time.sleep(2)
    print("It is time for you to rise up and dethrone her by stealing the source of her power,")
    #time.sleep(2)
    print("the recipie for the SCONE OF ENCHANTMENT!")
    #time.sleep(2)
    print("In your travels you will have to solve complexing puzzles,")
    #time.sleep(2)
    print("battle the most ferocious beasts and learn to become a master baker.\n")
    #time.sleep(2)
    print("Will you make it through these rigorous challenges?")
    #time.sleep(2)
    print("Find out now in...\n")
    #time.sleep(2)
    print(''' 

 _____                               __   _____                           
|  __ \                             / _| /  ___|                          
| |  \/ __ _ _ __ ___   ___    ___ | |_  \ `--.  ___ ___  _ __   ___  ___ 
| | __ / _` | '_ ` _ \ / _ \  / _ \|  _|  `--. \/ __/ _ \| '_ \ / _ \/ __|\n| |_\ \ (_| | | | | | |  __/ | (_) | |   /\__/ / (_| (_) | | | |  __/\__ \ \n \____/\__,_|_| |_| |_|\___|  \___/|_|   \____/ \___\___/|_| |_|\___||___/	

    \n\n ''')

    #time.sleep(4)

    #input(Style.BRIGHT + "Quest 1: Blood, Sweat and Tears\nFind all 4 ingredients to make the ultimate scone!\n" + Style.RESET_ALL)
    print("Quest: BLOOD, SWEAT AND TEARS\nFind your way to Mary Berry to make the ultimate scone!\n")


"""def init_rooms(rooms, puzzle_rooms, boss_rooms):
    This function randomly selects the puzzle rooms to be used in each location
    and updates the dict of rooms
    

    rand_rooms = random.sample(puzzle_rooms, 2)

    exits = [{"east": "room_boss_paul", "west": "room_centre"}, {"west": "room_boss_ms", "east": "room_centre"}]

    directions = ["east", "west"]

    for i in range(len(rand_rooms)):
        rand_rooms[i]["exits"] = exits[i]
        rooms["room_centre"]["exits"][directions[i]] = rand_rooms[i]["id"]
        boss_rooms[i]["exits"][list(reversed(directions))[i]] = rand_rooms[i]["id"]

    return rooms"""


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string).
    """

    item_list = []
    for i in items:
        item_list.append(i["name"])
    return(", ".join(item_list))


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names.
    """

    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.".
    """

    if items:
        print("You have " + list_of_items(items) + ".\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this).
    """

    # Display room name
    time.sleep(1)
    print("\n\n")
    #print(Fore.RED + Style.BRIGHT + "---------------------------- " + room["name"].upper() + " ----------------------------" + Style.RESET_ALL)
    print("---------------------------- " + room["name"].upper() + " ----------------------------")
    print("")
    # Display room description
    #print(Fore.YELLOW + room["description"] + Style.RESET_ALL)
    print(room["story"])
    print("")


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads.
    """

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.
    """

    #print(Style.BRIGHT + "GO " + direction.upper() + Style.NORMAL + " to " + leads_to + ".")
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."
    """

    #print(Fore.YELLOW + "You can:")
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")

    """for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop your " + item["name"] + ".")"""

    print("")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    """

    return chosen_exit in exits


def execute_go(direction, game_stage):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room

    if game_stage == 0 and current_room == rooms["room_centre"] and direction == "north":
        print("The door is locked, search the other rooms to find the keys.\n")
        return False
    elif game_stage == 1 and current_room == rooms["room_centre"] and direction == "north":
        print("The door is locked, you have 1 key, search the last room to find the final key.\n")
        return False
    else:
        if is_valid_exit(current_room["exits"], direction):
            current_room = move(rooms, current_room["exits"], direction)
            print("Moving to " + current_room["name"] + "...")
            return True
        else:
            print("You cannot go there.")
            return False


def execute_take(item_id_1, item_id_2 = ""):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    if item_id_2 != "":
        item_id = item_id_1 + " " + item_id_2
    else:
        item_id = item_id_1

    if any(d["id"] == item_id for d in current_room["items"]):
        for i in range(len(current_room["items"])):

            if item_id == current_room["items"][i]["id"]:
                inventory.append(current_room["items"][i])
                print("You take the " + current_room["items"][i]["name"] + "\n")
                (current_room["items"]).remove(current_room["items"][i])
                break

        return False

    else:
        print("You cannot take that.\n")
        return False
    

"""def execute_drop(item_id):
    This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."

    if any(d["id"] == item_id for d in inventory):
        for i in range(len(inventory)):

            if item_id == inventory[i]["id"]:
                (current_room["items"]).append(inventory[i])
                inventory.remove(inventory[i])
                print(item_id + " dropped.")
                break

        return True

    else:
        print("You cannot drop that.\n")
        return False"""
    

def execute_help():
    """If the player asks for help this function is executed. A brief list of possible
    commands are outputted to show the player what they can do, and a hint is printed
    if the player is stuck.
    """

    print(current_room["story"])


def execute_command(command, game_stage):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    if 0 == len(command):
        return False

    if command[0] == "go":
        if len(command) > 1:
            return execute_go(command[1], game_stage)
        else:
            print("Go where?\n")

    elif command[0] == "take":
        if len(command) > 1:
            if len(command) == 3:
                return execute_take(command[1], command[2])
            else:
                return execute_take(command[1])
        else:
            print("Take what?\n")

    elif command[0] == "help":
        execute_help()
        return False

    else:
        print("This makes no sense.\n")
        return False


def player_input():
    """The players's input is normalised using the normalise_input()
    function before being returned.
    """

    #print("What do you want to do?" + Style.RESET_ALL)
    print("What do you want to do?")

    # Read player's input
    #user_input = input("> " + Fore.CYAN)
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(rooms, exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction".
    """

    # Next room to go to
    return rooms[exits[direction]]


def execute_event(event):
    global current_room

    print_room(current_room)
    print_inventory_items(inventory)

    if event == "maze":
        maze_event(maze_rooms)
    elif event == "ms":
        boss_ms_event()
    elif event == "paul":
        boss_paul_event()
    elif event == "mary":
        boss_mary_event()
    elif event == "keypad":
        if game_stage == 0:
            rooms["room_centre"]["story"] = "You have returned to the room where you started. The arched doorway at the\nfar end of the room remains locked. You return to the vast, expansive room\nin the centre of the Red Velvet Keep. The room is airily chilling.\nThe air is filled with flour dust, illuminated by strands of light beaming in\nfrom the windows. The walls are adorned with paintings of baked goods and in\nthe centre is a stone statue of a croquembouche. On the far wall is a large,\narched doorway with two key holes. You have one of the keys."
        else:
            rooms["room_centre"]["story"] = "You have returned to the room where you started. The arched doorway at the\nfar end of the room remains locked. You return to the vast, expansive room\nin the centre of the Red Velvet Keep. The room is airily chilling.\nThe air is filled with flour dust, illuminated by strands of light beaming in\nfrom the windows. The walls are adorned with paintings of baked goods and in\nthe centre is a stone statue of a croquembouche. On the far wall is a large,\narched doorway with two key holes. You have both of the keys."
        keypad_event()
    elif event == "wordsearch":
        if game_stage == 0:
            rooms["room_centre"]["story"] = "You have returned to the room where you started. The arched doorway at the\nfar end of the room remains locked. You return to the vast, expansive room\nin the centre of the Red Velvet Keep. The room is airily chilling.\nThe air is filled with flour dust, illuminated by strands of light beaming in\nfrom the windows. The walls are adorned with paintings of baked goods and in\nthe centre is a stone statue of a croquembouche. On the far wall is a large,\narched doorway with two key holes. You have one of the keys."
        else:
            rooms["room_centre"]["story"] = "You have returned to the room where you started. The arched doorway at the\nfar end of the room remains locked. You return to the vast, expansive room\nin the centre of the Red Velvet Keep. The room is airily chilling.\nThe air is filled with flour dust, illuminated by strands of light beaming in\nfrom the windows. The walls are adorned with paintings of baked goods and in\nthe centre is a stone statue of a croquembouche. On the far wall is a large,\narched doorway with two key holes. You have both of the keys."
        wordsearch_event()


def maze_event(maze_rooms):
    global current_room

    maze_room = maze_rooms["maze_01"]
    smell = 0

    while True:
        if maze_room["weight"] != 13:
            if maze_room["weight"] > smell:
                print("The smell of baked bread gets STRONGER.")
                time.sleep(1)
            elif maze_room["weight"] < smell:
                print("The smell of baked bread gets WEAKER.")
                time.sleep(1)
            else:
                print("You can smell freshly baked bread in the distance.")

        smell = maze_room["weight"]

        if maze_room["id"] == "maze_44":
            current_room = move(rooms, current_room["exits"], "north")
            break

        print("\nYou can:")
        # Iterate over available exits
        for direction in maze_room["exits"]:
            # Print possible exits
            print("GO " + direction.upper())

        valid_input = False
        while not valid_input:
            # Ask the player for a response
            print("")
            command = player_input()


            if len(command) == 0 or command[0] != "go":
                print("You cannot do that.\n")
            else:
                if len(command) > 1:
                    if is_valid_exit(maze_room["exits"], command[1]):
                        maze_room = move(maze_rooms, maze_room["exits"], command[1])
                        print("Moving " + command[1] + "...\n")
                        valid_input = True
                    else:
                        print("You cannot go there.\n")
                else:
                    print("Go where?\n")


def boss_paul_event():
    global game_stage

    #Add combat stuff here
    combat(bosses["boss_paul"])

    #When boss is defeated:
    print("You have defeated Paul, you can now take their key!\n")

    game_stage += 1
    execute_take("key_1")
    del current_room["event"]
    current_room["story"] = "You are back in the walk-in freezer. Frozen confectionary lays scattered throughout\nthe room in the aftermath of your battle with Paul.\nThere is nothing of interest here."

    # Show the menu with possible actions
    print_menu(current_room["exits"], current_room["items"], inventory)

    valid_input = False
    while not valid_input:
        # Ask the player for a response
        command = player_input()

        # Execute the player's command
        valid_input = execute_command(command, game_stage)


def boss_ms_event():
    global game_stage
    
    #Add combat stuff here
    combat(bosses["boss_ms"])

    #When boss is defeated:
    print("You have defeated Mel and Sue, you can now take their key!\n")

    game_stage += 1
    execute_take("key_2")
    del current_room["event"]
    current_room["story"] = "You enter a narrow hallway. As you walk down the path you notice that it\nbecomes continually larger with each step you take. You are back in the Office,\nyou are relieved that the room now lays silent and empty.\nThere is nothing of interest here."

    # Show the menu with possible actions
    print_menu(current_room["exits"], current_room["items"], inventory)

    valid_input = False
    while not valid_input:
        # Ask the player for a response
        command = player_input()

        # Execute the player's command
        valid_input = execute_command(command, game_stage)


def boss_mary_event():
    global game_stage
    
    #Add combat stuff here
    combat(bosses["boss_mary"])

    #When boss is defeated:
    print("You have defeated Mary, you can now take her Super Secret Formula!\n")

    game_stage = 4
    execute_take("secret_formula")
    del current_room["event"]
    current_room["story"] = ""


def keypad_event():
    global current_room

    number = random.randrange (0,9) #random correct number in the range of 0-9 
    health = 100 #edit this to match game health variable name
    print ("You've encountered a keypad,")# edit this to cahnge introudction of puzzle 
    print ("You've already guessed the first three numbers from the keypad as flour was still on the keys.\n")
    print ("Now you must now guess the last digit:")

    while True:
        try:
            temp = int(input("> "))
            break
        except ValueError:
            print("\nYou can only input a number:")

    while temp != number:
        if temp > number: 
            print ("\nThe number may be SMALLER")
            health = health - 10
            print ("You have been shocked by the keypad. You lost 10 health, and you have",  health, "remaining")
            while True:
                try:
                    temp = int(input("Guess again:\n> "))
                    break
                except ValueError:
                    print("\nYou can only input a number:")
        else: 
            print("\nThe last number may be LARGER")
            health = health - 10
            print ("You have been shocked by the keypad. You lost 10 health, and you have",  health, "remaining")
            while True:
                try:
                    temp = int(input("Guess again:\n> "))
                    break
                except ValueError:
                    print("\nYou can only input a number:")
    print("\nYou have correctly guessed the numberpad code. The door ahead opens rapidly!") #Discription for completing the puzzle

    del current_room["event"]
    current_room["story"] = "You descend into the under belly of Mary's fortress of pain. Once again you find\nyourself lurking in the cellar. It's dark and damp, the only light is coming from a few\nflickering candles hung on the walls. Empty crates and wooden pallets scatter the room.\nYou ask yourself why you chose to come back here?"
    current_room = move(rooms, current_room["exits"], "west")

    #return health


def wordsearch_event():
    global current_room

    print("You are stuck at a door. This door requires a keyword to open the door")
    print("You notice on the wall next to the door is a cluster of random letters written in flour,")
    print("from this you must figure out the key word to open the door\n")# Discription of the puzzle 
    print("The wall reads:")
    print(" S A B M A Y R")
    print(" Z C A R T Y A") ### Here is the wordsearch 
    print(" R R O C K O N")
    print(" Y Y X N K L N")
    print(" L A M C E P O\n")

    entry = str(input("> ")) 
    while entry.upper() != "SCONE": # loops until SCONE is entered. 
        if entry == "hint": #Game also offers a hint
            print ("\nYou think to yourself... the keyword must be delicious!")
            entry = str(input("> "))
        else:
            print ("\nTry again, this is the incorrect password:")
            entry = str(input("> "))
    print ("You have found the correct word. The door ahead opens rapidly!") # Discription upon completion

    del current_room["event"]
    current_room["story"] = "You are back in the pantry. Surrounding you from all directions are shelves towering\nall the way to the ceiling, stacked full of pastries, cakes, loafs of bread and\na plethora of cooking ingredients. You are reminded of the wordsearch that you\ncompleted and your stomach rumbles. 'Mmm scones...'"
    current_room = move(rooms, current_room["exits"], "east")


def combat(enemy):               #this code currently serves as a basic framework for what I think should be possible with the combat system. However I can't really go too deep without seeing what else is going on in the program.
    
    turn = 0                #Initialise setup variables. Ensure turn and player_turn are reset.
    player_turn = False
    retreat = False

    while ((player["health"] > 0) and (enemy["health"] > 0) and (retreat == False)):                     #Until someone dies or retreats, repeat
        time.sleep(1)
        
        if (turn == 0 and player["speed"] > enemy["speed"]) or (player_turn == True):                             #if players turn
            player_input = input("What do you want to do?\n")
                       
            if player_input == "attack":                                                                        #if player tries to attack
                player_attack(player["strength"], player["dexterity"], enemy)
                turn = turn + 1
                player_turn = False
      
            elif player_input == ("retreat" or "run away" or "run"):                                            #if player tries to run
                retreat = evacuate(player["speed"], enemy["speed"])
                turn = turn + 1
                player_turn = False

            else:
                print("You can't do that.")

        else:
            print(enemy["name"], "was faster than you and attakced first!")                                                                                           #if enemies turn
            enemy_attack(player["speed"], enemy)
            player_turn = True

    if player["health"] > 0 and retreat == False:                                   #This code handles what happens to the player after the encounter based on if they won, lost or ran.
            victory(enemy)
    elif player["health"] <= 0:
            defeat()


def player_attack(player_strength, player_dexterity, enemy):  #if the player attacks          
    hit_chance = ((player_dexterity - enemy["speed"]) * 10) + (random.random() * 0.75 * 100)                            #calculate chance for player to hit

    if (hit_chance >= 50) and (player["equipped"]["id"] == enemy["weakness"]):                                             #if player hits and is using weapon enemy weak to.
        player_attack = int(round(player_strength * 2 + 3 * random.uniform(0.8, 1.2)))                       #calculate damage done by player. Base strength multiplied by 2 due to enemy_weakness, +-20%
        enemy["health"] = enemy["health"] - player_attack                                       #inflict damage
            
        print("You attack " + enemy["name"] + " for " + str(player_attack) + " points of damage.")                   #inform player of damage dealt
        time.sleep(2)
        print(enemy["name"] + " has " + str(enemy["health"]) + " hitpoints remaining.")

    elif hit_chance >= 50:                                                                               #if player hits
        player_attack = int(round(player_strength + 3 * random.uniform(0.8, 1.2)))                                                 #calculate damage done by player. Base strength, +-20%
        enemy["health"] = enemy["health"] - player_attack                                       #inflict damage
            
        print("You attack " + enemy["name"] + " for " + str(player_attack) + " points of damage.")                   #inform player of damage dealt
        time.sleep(2)
        print(enemy["name"] + " has " + str(enemy["health"]) + " hitpoints remaining.")
        
    else:
        print("You missed!")
        time.sleep(1)

    if enemy["health"] < 0:
        enemy["health"] = 0

                          
def enemy_attack(player_speed, enemy):                           #During an enemy turn
    hit_chance = ((enemy["dexterity"] - player_speed) * 10) + (random.random() * 100)                    #calculate chance for enemy to hit
                              
    if hit_chance >= 50:
        enemy_attack = int(round(enemy["strength"] * random.uniform(0.8, 1.2)))
        player["health"] = player["health"] - enemy_attack                                            #If then enemy hits the player. Damage = to enemystrength value +-20%
                  
        print(enemy["name"] + " attacks you for " + str(enemy_attack) + " points of damage.")            #inform player of damage dealt
        if player["health"] < 0:
            player["health"] = 0
        time.sleep(2)
        print("You have " + str(player["health"]) + " hitpoints remaining.")
                          
    else:
        print(enemy["name"] + " attacked you, but missed")                                         #inform the player they got lucky and increment the turn


def evacuate(player_speed, enemy_speed):                                           #if player tries to retreat
    retreat = False
    
    if player_speed > (enemy_speed + 1):                                                        #if player is 2 points faster, they escape
        retreat = True
        print("You easily get away")
        return (retreat)

    elif (player_speed + 1) < enemy_speed:                                                      #if player is 2 points slower, they cant escape and end the turn.
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


def victory(enemy):                                                                            #This function should be run in the event the player defeats an enemy.
    print ("YOU DEFEATED " + enemy["name"]) #+ ".\nYOU RECIEVED: " + enemy["items"])
    #inventory.append(enemy["items"])                                                                     #player recieves reward for defeating the enemy


def defeat():                                                                               #This function should be run in the event the player dies
    print("YOU DIED. THE HOLY SCONE WILL NEVER BE FINISHED. THE WORLD WILL END.")
    time.sleep(2)
    player_input = input("Would you like to restart? (y/n)")
    if player_input.lower() == ("y"):
        os.execl(sys.executable, sys.executable, * sys.argv)                                    #restarts the program
    elif player_input.lower() == ("n"):
        exit()



# This is the entry point of our program
def main():

    #rooms = init_rooms(rooms, puzzle_rooms, boss_rooms)
    opening()

    # Main game loop
    running = True
    while running:

        if "event" in current_room.keys():
            execute_event(current_room["event"])
        else:
            valid_input = False

            # Display game status (room description, inventory etc.)
            print_room(current_room)
            print_inventory_items(inventory)

            while not valid_input:
                # Show the menu with possible actions
                print_menu(current_room["exits"], current_room["items"], inventory)
                # Ask the player for a response
                command = player_input()
                # Execute the player's command
                valid_input = execute_command(command, game_stage)

        if game_stage == 4:
            running = False

    print("\nUsing Mary's secret formula, you bake the world's best scone!\n****************** You win! ******************")

            



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

#!/usr/bin/python3

import random

from map import rooms, puzzle_rooms, boss_rooms
from maze import maze_rooms

from player import *
from items import *
from gameparser import *
#from colorama import Fore, Back, Style



def opening():
    """This function prints all of the opening text for the game.
    """
    #input(Fore.YELLOW + Style.BRIGHT + "\nWelcome!\n" + Style.NORMAL)
    input("\nWelcome!\n")
    print("In a world where baking is the only form of solice, one chef strives to please the formidable Mary Berry,")
    input("you have set yourself on a quest to source the rarest ingrediants in all four kingdoms.")
    print("In your travels you will have to solve complexing puzzles,")
    input("battle the most ferocious beasts and bake the tastiest scone the world has ever known.\n")
    print("Will you make it through these rigorous challenges?")
    print("Find out now in...\n")
    input("Game of Scones!\n\n")

    #input(Style.BRIGHT + "Quest 1: Blood, Sweat and Tears\nFind all 4 ingredients to make the ultimate scone!\n" + Style.RESET_ALL)
    input("Quest 1: BLOOD, SWEAT AND TEARS\nFind all 4 ingredients to make the ultimate scone!\n")


def init_rooms(rooms, puzzle_rooms, boss_rooms):
    """This function randomly selects the puzzle rooms to be used in each location
    and updates the dict of rooms
    """

    rand_rooms = random.sample(puzzle_rooms, 2)

    exits = [{"east": "room_boss_paul", "west": "room_centre"}, {"west": "room_boss_ms", "east": "room_centre"}]

    directions = ["east", "west"]

    for i in range(len(rand_rooms)):
        rand_rooms[i]["exits"] = exits[i]
        rooms["room_centre"]["exits"][directions[i]] = rand_rooms[i]["id"]
        boss_rooms[i]["exits"][list(reversed(directions))[i]] = rand_rooms[i]["id"]

    return rooms


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
    print("")
    #print(Fore.RED + Style.BRIGHT + "-------------------------- " + room["name"].upper() + " --------------------------" + Style.RESET_ALL)
    print("-------------------------- " + room["name"].upper() + " --------------------------")
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


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room

    if is_valid_exit(current_room["exits"], direction):
        current_room = move(rooms, current_room["exits"], direction)
        print("Moving to " + current_room["name"] + "...")
        return True
    else:
        print("You cannot go there.")
        return False


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    if any(d["id"] == item_id for d in current_room["items"]):
        for i in range(len(current_room["items"])):
            
            if item_id == current_room["items"][i]["id"]:
                inventory.append(current_room["items"][i])
                (current_room["items"]).remove(current_room["items"][i])
                print(item_id + " taken.")
                break

        return True

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


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    if 0 == len(command):
        return False

    if command[0] == "go":
        if len(command) > 1:
            return execute_go(command[1])
        else:
            print("Go where?\n")

    elif command[0] == "take":
        if len(command) > 1:
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


def execute_event(event, last_commad):
    global current_room

    if event == "maze":
        maze_event(maze_rooms, last_commad)
    elif event == "maze complete":
        print("You work your way back through the maze to the centre room.")
        current_room = rooms["room_centre"]
    elif event == "boss":
        boss1_event()
    elif event == "trivia":
        trivia_event()


def maze_event(maze_rooms, last_commad):
    global current_room

    print("")
    print_room(current_room)
    print_inventory_items(inventory)

    maze_room = maze_rooms["maze_01"]
    smell = 0

    while True:
        if maze_room["weight"] > smell:
            print("The smell of baked bread gets stronger.")
        elif maze_room["weight"] < smell:
            print("The smell of baked bread gets weaker.")
        else:
            print("You can smell freshly baked bread in the distance.")

        smell = maze_room["weight"]

        if maze_room["id"] == "maze_44":
            current_room["event"] = "maze complete"
            current_room = move(rooms, current_room["exits"], last_commad[1])
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
                        print("You cannot go there.")
                else:
                    print("Go where?\n")


def boss1_event():
    print_room(current_room)
    print_inventory_items(inventory)
    
    #Add combat stuff here
    input("Press enter to fight the boss!")

    #When boss is defeated:
    print("You have defeated the boss, you can now take their loot!\n")
    del current_room["event"]

    # Show the menu with possible actions
    print_menu(current_room["exits"], current_room["items"], inventory)

    valid_input = False
    while not valid_input:
        # Ask the player for a response
        command = player_input()

        # Execute the player's command
        valid_input = execute_command(command)


def trivia_event():
    print_room(current_room)
    print_inventory_items(inventory)

    input("Trivia question")

    print("Correct! You may continue on your quest.")
    del current_room["event"]

    print_menu(current_room["exits"], current_room["items"], inventory)

    valid_input = False
    while not valid_input:
        # Ask the player for a response
        command = player_input()

        # Execute the player's command
        valid_input = execute_command(command)


# This is the entry point of our program
def main():
    global rooms

    rooms = init_rooms(rooms, puzzle_rooms, boss_rooms)
    opening()

    # Main game loop
    running = True
    while running:

        if "event" in current_room.keys():
            execute_event(current_room["event"], last_commad)
        else:
            valid_input = False

            # Display game status (room description, inventory etc.)
            print_room(current_room)
            print_inventory_items(inventory)

            # Show the menu with possible actions
            print_menu(current_room["exits"], current_room["items"], inventory)

            while not valid_input:
                # Ask the player for a response
                command = player_input()
                last_commad = command
                # Execute the player's command
                valid_input = execute_command(command)

        if len(inventory) == 4 and current_room == rooms["room_centre"]:
            running = False

    print("\nYou return to the oven and bake the world's best scone!\n****************** You win! ******************")

            



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
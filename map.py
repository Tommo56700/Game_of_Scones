from items import *

#This needs to be heavily updated

room_centre = {
    "id": "room_centre",

    "name": "Main Baking Room",

    "story": "*** description ***",

    "exits": {"north": "room_puzzle_maze"},

    "items": []
}

room_puzzle_maze = {
    "id": "room_puzzle_maze",

    "name": "Store Room",

    "story": "You try to push the door open but it wont budge, there is something heavy behind it.\nIt's as if something is holding the door...\nYou push with all of your strength...\nThe door gives, and you barge into a dark storeroom filled to the roof with boxes.\nThere is a makeshift path, but you can't see a clear way through.\nIn the distance you can smell freshly baked bread.\n\nMiniquest: FOLLOW YOUR NOSE\nFind your way through the maze of boxes!",

    "exits":  {"north": "room_boss_mary", "south": "room_centre"},

    "items": [],

    "event": "maze"
}

room_puzzle_2 = {
    "id": "",

    "name": "Sue's Cellar",

    "story": "*** description ***",

    "exits": {},

    "items": []
}

room_puzzle_3 = {
    "id": "",

    "name": "Paul's Pantry",

    "story": "*** description ***",

    "exits": {},

    "items": []
}

room_puzzle_4 = {
    "id": "",

    "name": "Dough Room",

    "story": "*** description ***",

    "exits": {},

    "items": []
}

room_puzzle_5 = {
    "id": "",

    "name": "Proving Room",

    "story": "*** description ***",

    "exits": {},

    "items": []
}

room_puzzle_trivia = {
    "id": "",

    "name": "Walk-in Freezer",

    "story": "*** description ***",

    "exits": {},

    "event": "trivia",

    "items": []
}

room_boss_mary = {
    "id": "room_boss_mary",

    "name": "boss_1",

    "story": "*** story ***",

    "exits": {"south": "room_puzzle_maze"},

    "event": "boss",

    "items": [item_flour]
}

room_boss_2 = {
    "id": "room_boss_2",

    "name": "boss_2",

    "story": "*** description ***",

    "exits": {},

    "event": "boss",

    "items": [item_butter]
}

room_boss_3 = {
    "id": "room_boss_3",

    "name": "boss_3",

    "story": "*** description ***",

    "exits": {},

    "event": "boss",

    "items": [item_milk]
}

room_boss_4 = {
    "id": "room_boss_4",

    "name": "boss_4",

    "story": "*** description ***",

    "exits": {},

    "event": "boss",

    "items": [item_eggs]
}


rooms = {
    "room_centre": room_centre,
    "room_puzzle_maze": room_puzzle_maze,
    "room_boss_mary": room_boss_mary,
    "room_boss_2": room_boss_2,
    "room_boss_3": room_boss_3,
    "room_boss_4": room_boss_4
}

puzzle_rooms = [room_puzzle_2, room_puzzle_3, room_puzzle_4, room_puzzle_5, room_puzzle_trivia]
from items import *

#This needs to be heavily updated

room_centre = {
    "name": "centre",

    "description": "*** description ***",

    "exits": {"north": "puzzle_maze", "east": "puzzle_2", "south": "puzzle_3", "west": "puzzle_4"},

    "items": []
}

room_puzzle_maze = {
    "name": "puzzle_maze",

    "description": "*** description ***",

    "exits":  {"north": "boss_1", "south": "centre"},

    "items": []
}

room_puzzle_2 = {
    "name": "puzzle_2",

    "description": "*** description ***",

    "exits": {"east": "boss_2", "west": "centre"},

    "items": []
}

room_puzzle_3 = {
    "name": "puzzle_3",

    "description": "*** description ***",

    "exits": {"south": "boss_3", "north": "centre"},

    "items": []
}

room_puzzle_4 = {
    "name": "puzzle_4",

    "description": "*** description ***",

    "exits": {"west": "boss_4", "east": "centre"},

    "items": []
}

room_boss_1 = {
    "name": "boss_1",

    "description": "*** description ***",

    "exits": {"south": "puzzle_maze"},

    "items": [item_flour]
}

room_boss_2 = {
    "name": "boss_2",

    "description": "*** description ***",

    "exits": {"west": "puzzle_2"},

    "items": [item_butter]
}

room_boss_3 = {
    "name": "boss_3",

    "description": "*** description ***",

    "exits": {"north": "puzzle_3"},

    "items": [item_milk]
}

room_boss_4 = {
    "name": "boss_4",

    "description": "*** description ***",

    "exits": {"east": "puzzle_4"},

    "items": [item_eggs]
}


rooms = {
    "centre": room_centre,
    "puzzle_maze": room_puzzle_maze,
    "puzzle_2": room_puzzle_2,
    "puzzle_3": room_puzzle_3,
    "puzzle_4": room_puzzle_4,
    "boss_1": room_boss_1,
    "boss_2": room_boss_2,
    "boss_3": room_boss_3,
    "boss_4": room_boss_4
}

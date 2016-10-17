from items import *

#This needs to be heavily updated

room_centre = {
    "id": "room_centre",

    "name": "Main Baking Room",

    "story": "You have infiltrated the lair of the queen, but be careful not to wake the beast.\nThe journey here so far has been a long and challenging one, but things are\nabout to get harder. You find yourself standing in a vast, expansive room in\nthe centre of the Red Velvet Keep, the palace from which Mary Berry pulls the\nstrings over the Seven Kingdoms. The room is airily chilling.\nThe air is filled with flour dust, illuminated by strands of light beaming in\nfrom the windows. The walls are adorned with paintings of baked goods and in\nthe centre is a stone statue of a croquembouche.  On the far wall is a large,\narched doorway with two key holes. One appears to be made from ginger bread,\nthe other from shortbread. On one side is a door labelled Pantry. Whilst, on the\nother side is a door labelled Cellar, and a stairway leading down.",

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

room_puzzle_keypad = {
    "id": "room_puzzle_keypad",

    "name": "The Cellar",

    "story": "You descend into the under belly of Mary’s fortress of pain. The cellar is dark\nand damp, the only light coming from a few flickering candles hung on the walls.\nEmpty crates and wooden pallets scatter the room. You notice on the floor an\nelaborate rug, an heirloom of the Berry family no doubt. One of the corners is\nupturned slightly. On the far wall is a door labelled store room.",

    "exits": {},

    "items": [] #combat item
}

room_puzzle_crossword = {
    "id": "room_puzzle_crossword",

    "name": "Paul's Pantry",

    "story": "You are in the pantry. Surrounding you from all directions are shelves towering\nall the way to the ceiling, stacked full of pastries, cakes, loafs of bread and\na plethora of cooking ingredients. You notice a chest with the lid slightly\najar. On the far wall is a large freezer door.",

    "exits": {},

    "items": [] #combat item
}


room_boss_mary = {
    "id": "room_boss_mary",

    "name": "Mary's Kitchen",

    "story": "You have made it this far but you must now rely on your baking ability more\nthan ever. This is it. The final showdown. The stage is set, the show must now\nunfold. And the far end of the room is a great fiery furnace, the heat from\nwhich is scolding even from this distance. You have well and truly descended\ninto Mary’s hell. In front of the furnace you see four ingredients laid out on a\ntable; milk, flour, butter and eggs. But there in front of you is a sight that\nfills you with dread, 5 feet and 3 inches of the pastry queen herself. She stairs\nyou dead in the eye, points are you with her bony finger and an evil, wry smile\nspreads across her face.",

    "exits": {"south": "room_puzzle_maze"},

    "event": "boss",

    "items": [] #Super Secret Formula ITEM/WINNING
}

room_boss_paul = {
    "id": "room_boss_paul",

    "name": "Freezer",

    "story": "You enter the walk in freezer. Immediately you are chilled to your core, but not\nbecause of the temperature, but instead because of what stands in front of you.\nA zombie like Paul Hollywood stands with his arms crossed, staring coldly at you.\nHis eyes black and cavernous. His heart has been turned to ice Mary Berry and now\nhis only sanctuary is in the confines of the  walk in freezer. You notice in his\nback pocket that there's a key made from ginger bread.",

    "exits": {},

    "event": "boss",

    "items": [] #Ginger KEY ITEM
}

room_boss_ms = {
    "id": "room_boss_ms",

    "name": "Mel and Sue's office",

    "story": "You enter the store room. As you walk down a narrow hallway you notice that it\n becomes continually larger with each step you take. You can hear a mumbling of \nvoices which get louder and clearer as you approach the room. There you find Mel \nand Sue cracking jokes full of innuendo, some so bad that it pains your ears. It \ntakes them a moment to notice you but they then fall silent as they turn to face \nyou, their eyes piercing like daggers in your chest. You notice a key made of \nshort bread in Mel’s jacket pocket. ",

    "exits": {},

    "event": "boss",

    "items": [] #Shortbread KEY ITEM
}



rooms = {
    "room_centre": room_centre,
    "room_puzzle_keypad": room_puzzle_keypad,
    "room_puzzle_crossword": room_puzzle_crossword,
    "room_puzzle_maze": room_puzzle_maze,
    "room_boss_mary": room_boss_mary,
    "room_boss_paul": room_boss_paul,
    "room_boss_ms": room_boss_ms
}

puzzle_rooms = [room_puzzle_keypad, room_puzzle_crossword]

boss_rooms = [room_boss_paul, room_boss_ms, room_boss_mary]


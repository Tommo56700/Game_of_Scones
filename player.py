from items import *
from map import rooms

inventory = [item_wooden_spoon]

# Start game at the reception
current_room = rooms["room_centre"]

player = {
    "name": "",

    "health": 0,

    "speed": 0,

    "strength": 0,

    "dexterity": 0,

    "equipped": item_wooden_spoon
}
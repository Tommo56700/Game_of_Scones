from items import *
from map import rooms

inventory = [item_wooden_spoon]

# Start game at the reception
current_room = rooms["room_centre"]

player = {
    "name": "",

    "health": 20,

    "speed": 5,

    "strength": 10,

    "dexterity": 10,

    "equipped": item_wooden_spoon
}
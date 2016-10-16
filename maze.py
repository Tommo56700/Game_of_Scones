maze_01 = {
    "id": "maze_01",

    "story": "*** description ***",

    "weight": 0,

    "exits": {"north": "maze_11"}
}

maze_10 = {
    "id": "maze_10",

    "story": "*** description ***",

    "weight": 1,

    "exits": {"east": "maze_11"}
}

maze_11 = {
    "id": "maze_11",

    "story": "*** description ***",

    "weight": 4,

    "exits": {"north": "maze_21", "east": "maze_12", "south": "maze_01", "west": "maze_10"}
}

maze_12 = {
    "id": "maze_12",

    "story": "*** description ***",

    "weight": 3,

    "exits": {"east": "maze_13", "west": "maze_11"}
}

maze_13 = {
    "id": "maze_13",

    "story": "*** description ***",

    "weight": 2,

    "exits": {"west": "maze_12"}
}

maze_21 = {
    "id": "maze_21",

    "story": "*** description ***",

    "weight": 5,

    "exits": {"north": "maze_31", "south": "maze_11"}
}

maze_24 = {
    "id": "maze_24",

    "story": "*** description ***",

    "weight": 11,

    "exits": {"north": "maze_34"}
}

maze_30 = {
    "id": "maze_30",

    "story": "*** description ***",

    "weight": 6,

    "exits": {"east": "maze_31"}
}

maze_31 = {
    "id": "maze_31",

    "story": "*** description ***",

    "weight": 8,

    "exits": {"north": "maze_41", "east": "maze_32", "south": "maze_21", "west": "maze_30"}
}

maze_32 = {
    "id": "maze_32",

    "story": "*** description ***",

    "weight": 9,

    "exits": {"east": "maze_33", "west": "maze_31"}
}

maze_33 = {
    "id": "maze_33",

    "story": "*** description ***",

    "weight": 10,

    "exits": {"east": "maze_34", "west": "maze_32"}
}

maze_34 = {
    "id": "maze_34",

    "story": "*** description ***",

    "weight": 12,

    "exits": {"north": "maze_44", "south": "maze_24", "west": "maze_33"}
}

maze_41 = {
    "id": "maze_41",

    "story": "*** description ***",

    "weight": 7,

    "exits": {"south": "maze_31"}
}

maze_44 = {
    "id": "maze_44",

    "story": "*** description ***",

    "weight": 13,

    "exits": {"south": "maze_34"}
}


maze_rooms = {
            "maze_01": maze_01,
            "maze_10": maze_10,
            "maze_11": maze_11,
            "maze_12": maze_12,
            "maze_13": maze_13,
            "maze_21": maze_21,
            "maze_24": maze_24,
            "maze_30": maze_30,
            "maze_31": maze_31,
            "maze_32": maze_32,
            "maze_33": maze_33,
            "maze_34": maze_34,
            "maze_41": maze_41,
            "maze_44": maze_44
}
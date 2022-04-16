import json
import os
from objects.room import Room


def load_rooms():
    """
    Finds all of the json files in the rooms folder and
    turns them into Room objects. All of the items and doors
    in the file are also turned into Item objects and Door
    objects, respectively.
    Returns a dictionary of all of the Room objects with
    their names as keys.
    """
    # empty dictionary to store Rooms in
    room_dict = {}

    # 1. Get list of json files in rooms folder.
    room_files = os.listdir(os.path.abspath("rooms"))

    # 2. For each file:
    for file in room_files:
        with open(file) as room_json:
            # 1. Turn JSON into a Python dictionary.
            room_data = json.load(room_json)

            # 2. Create a Room object with the given dictionary with empty
            #   items and doors dictionaries.

            # 3. Turn each item into an Item object and add it to the room.
            # 4. Turn each door into a Door object and add it to the room.
            # 5. Add Room to room_dict.

    # 3. Return dictionary of Rooms
    return room_dict

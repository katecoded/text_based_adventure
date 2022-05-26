import json
import os
import jsonschema

from objects.room import Room
from objects.item import Item
from objects.door import Door


def validate_schema(json_data):
    """
    Raises a ValidationError if any of the given json_data
    does not match the room schema.
    """

    # create the schema to compare the room files to
    room_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "short_description": {"type": "string"},
            "long_description": {"type": "string"},
            "doors": {
                "type": "object",
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "destination": {"type": "string"},
                        "direction": {"type": "string"},
                        "key": {"type": "string"},
                        "locked": {"type": "boolean"},
                        "description": {"type": "string"}
                        "hidden": {"type": "boolean"}
                    },
                    "additionalProperties": False,
                    "required": ["destination", "direction", "key",
                                 "locked", "description"]
                }
            },
            "items": {
                "type": "object",
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "description": {"type": "string"},
                        "takeable": {"type": "boolean"},
                        "type": {"type": "string"}
                        "hidden": {"type": "boolean"}
                    },
                    "additionalProperties": False,
                    "required": ["description", "takeable", "type"]
                },
            }
        },
        "additionalProperties": False,
        "required": ["name", "short_description", "long_description",
                     "doors", "items"]
    }

    # validate the data against the schema
    jsonschema.validate(json_data, room_schema)


def create_object_dictionary(object_data, object_type):
    """
    Takes a dictionary of data for either items or doors
    and returns a dictionary of the objects of the
    specified type with the names as keys.
    """
    result_dict = {}

    # for each key, create a game object of the specified type and
    # add it to the dictionary
    for name in object_data.keys():
        if object_type == "item":
            item = Item(name, object_data[name]["description"],
                        object_data[name]["takeable"],
                        object_data[name]["type"])
            if "hidden" in object_data[name] and object_data[name]["hidden"]:
                hidden_dict[name] = item
            else:
                result_dict[name] = item
        else:
            door = Door(name, object_data[name]["destination"],
                        object_data[name]["direction"],
                        object_data[name]["key"],
                        object_data[name]["description"])
            if "hidden" in object_data[name] and object_data[name]["hidden"]:
                hidden_dict[name] = door
            else:
                result_dict[name] = door

    return result_dict


def load_rooms(directory="rooms"):
    """
    Finds all room JSON files in the given folder (rooms is
    the default) and turns them into Room objects.
    All the items and doors in the file are also turned into
    Item objects and Door objects, respectively.
    Returns a dictionary of all the Room objects with
    their names as keys.
    :directory: A String directory name.
    """
    room_dict = {}

    # throw error if directory is not rooms or saves directory
    if directory != "rooms" and directory != "saves":
        raise Exception("Directory must be rooms or saves")

    # get list of all files in the given folder.
    room_files = os.listdir(os.path.abspath(directory))

    # iterate through each file of room data
    for file in room_files:

        # skip non-JSON files
        if not file.endswith(".json"):
            continue

        # get the relative path to the room data file and open it
        file_path = directory + "/" + file
        with open(file_path) as room_json:

            # load and validate room data
            room_data = json.load(room_json)
            validate_schema(room_data)

            # create Item object and Room object dictionaries
            items, hidden_items = create_object_dictionary(room_data["items"], "item")
            doors, hidden_doors = create_object_dictionary(room_data["doors"], "door")

            # merges hidden item and door dictionaries into one
            hidden_objects = {**hidden_items, **hidden_doors}

            # create a Room object with the Item and Door dictionaries
            room_dict[room_data["name"]] = Room(room_data["name"],
                                                room_data["short_description"],
                                                room_data["long_description"],
                                                doors, items, hidden_objects)

    return room_dict


if __name__ == "__main__":
    load_rooms()

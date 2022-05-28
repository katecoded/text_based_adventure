from objects.game import Game
from objects.room import Room
from objects.item import Item
from objects.door import Door
import json


def save_door_data(room, door):
    name = door.get_name()
    room["doors"][name] = {
        "destination": door.get_destination(),
        "direction": door.get_direction(),
        "key": door.get_key(),
        "locked": door.get_lock_status(),
        "description": door.get_description()
    }
    return


def save_item_data(room, item):
    name = item.get_name()
    room["items"][name] = {
        "description": item.get_description(),
        "takeable": item.is_takeable(),
        "type": item.get_type()
    }
    return


def make_json(curr):
    name = curr.get_name()
    doors = curr.get_doors()
    items = curr.get_items()
    room_data = {
        "name": name,
        "short_description": curr.get_short_description(),
        "long_description": curr.get_long_description(),
        "doors": {

        },
        "items": {

        }
    }
    for value in list(doors.values()):
        save_door_data(room_data, value)
    for value in list(items.values()):
        save_item_data(room_data, value)
    json_output = json.dumps(room_data, indent=4)

    name = name.lower()
    name = name.replace(" ", "_")
    filepath = "saves/" + name + ".json"
    with open(filepath, 'w') as outfile:
        outfile.write(json_output)
    outfile.close()
    return


def add_player_items(dict, item):
    name = item.get_name()
    dict[name] = {
        "description": item.get_description(),
        "takeable": item.is_takeable(),
        "type": item.get_type()
    }
    return


def create_save(gamestate):
    location = gamestate.get_current_room()
    location = location.get_name()
    with open("saves/player_loc.txt", "w") as outfile:
        outfile.write(location)
    outfile.close()

    rooms = gamestate.get_all_rooms()
    for value in list(rooms.values()):
        make_json(value)

    items = gamestate.get_inventory()
    inventory = {

    }
    for value in list(items.values()):
        add_player_items(inventory, value)

    json_output = json.dumps(inventory, indent=4)
    with open("saves/inventory.json", 'w') as outfile:
        outfile.write(json_output)
    outfile.close()

    return

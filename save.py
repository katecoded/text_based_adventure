import json

from objects.item import Item


def save_door_data(room, door):
    """
    Saves the given Door object's data as a dictionary
    within the given room's dictionary.
    :room: A dictionary representing a room.
    :door: A Door object.
    """
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
    """
    Saves the given Item object's data as a dictionary
    within the given room's dictionary.
    :room: A dictionary representing a room.
    :item: An Item object.
    """
    name = item.get_name()
    room["items"][name] = {
        "description": item.get_description(),
        "takeable": item.is_takeable(),
        "type": item.get_type()
    }
    return


def save_hidden_objects(room_data, hidden_objects):
    """
    Saves the given room's hidden objects.
    :room_data: A dictionary of room data.
    :hidden_objects: A dictionary of Item and Door objects.
    """
    for object in hidden_objects.values():
        if isinstance(object, Item):
            save_item_data(room_data, object)
            room_data["items"][object.get_name()]["hidden"] = True
        else:
            save_door_data(room_data, object)
            room_data["doors"][object.get_name()]["hidden"] = True


def make_json(curr):
    """
    Converts and saves the curr Room object as a JSON file.
    :curr: A Room object.
    """
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

    # save doors and items
    for value in list(doors.values()):
        save_door_data(room_data, value)
    for value in list(items.values()):
        save_item_data(room_data, value)
    # save hidden doors and items
    if curr.get_hidden_objects():
        save_hidden_objects(room_data, curr.get_hidden_objects())
    # save visited rooms
    if curr.get_visited():
        room_data["visited"] = True

    json_output = json.dumps(room_data, indent=4)
    name = name.lower()
    name = name.replace(" ", "_")
    filepath = "saves/" + name + ".json"
    with open(filepath, 'w') as outfile:
        outfile.write(json_output)
    outfile.close()
    return


def add_player_items(dict, item):
    """
    Saves the given Item object to a dictionary
    representing the player's inventory.
    :dict: A dictionary representing the inventory.
    :item: An Item object.
    """
    name = item.get_name()
    dict[name] = {
        "description": item.get_description(),
        "takeable": item.is_takeable(),
        "type": item.get_type()
    }
    return


def create_save(gamestate):
    """
    Saves the current state of the game including the current state
    of all rooms, the player's inventory, and the player's current
    location.
    :gamestate: A Game object.
    """
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

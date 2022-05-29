from objects.item import Item
import load_rooms
import json


def fill_inventory(held_items, gamestate):
    """
    Adds items in to player inventory after reading inventory dictionary from inventory.json
    """
    gamestate.reset_inventory()
    for name in held_items.keys():
        inv_item = Item(name, held_items[name]["description"],
                        held_items[name]["takeable"],
                        held_items[name]["type"])
        gamestate.add_item_to_inventory(name, inv_item)
    return


def load_game(gamestate):
    """
    Loads previously saved gamestate
    """
    # set rooms to previous state
    gamestate.set_all_rooms(load_rooms.load_rooms("saves"))
    # set players current location
    file = open('saves/player_loc.txt', 'r')
    location = file.readline()
    gamestate.set_current_room(location)
    file.close()
    # set player inventory
    file_2 = open('saves/inventory.json')
    held_items = json.load(file_2)
    fill_inventory(held_items, gamestate)
    file_2.close()
    return

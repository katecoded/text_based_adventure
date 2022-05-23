from objects.item import Item
from objects.door import Door
import random
# from objects.game import Game

non_interactive_actions = ["inventory", "help", "look", "savegame", "loadgame"]
pickup_actions = ["take", "grab", "get", "pickup"]
movement_actions = ["go", "move", "travel"]
drop_actions = ["drop", "remove"]
open_actions = ["open", "unlock"]
use_actions = ["use", "utilize"]
eat_actions = ["eat", "consume", "drink"]
examine_actions = ["lookat", "examine"]
combine_actions = ["combine"]

all_available_actions = non_interactive_actions + pickup_actions + \
                        movement_actions + eat_actions + drop_actions + \
                        use_actions + open_actions + \
                        examine_actions + combine_actions
prepositions = ["on", "upon", "at", "to", "with", "using"]
# prepositions = ["in", "at", "to", "with", "toward", "towards", "on", "into", "onto"]
# directions = ["north", "south", "east", "west"]  # up/down?


def pre_process_commands(input):
    """
    Preprocesses user input to combine two word commands into one word
    Changes look at into lookat and pick up into pickup
    """
    refined_input = input.replace("look at", "lookat", 1)
    return refined_input.replace("pick up", "pickup", 1)


def tokenize(input):
    """
    Splits user input into tokens and converts tokens to lowercase
    """
    token_list = input.split()
    token_list = [token.lower() for token in token_list]
    return token_list


def logic_splitter(token_list):
    """
    Splits tokenized user input into a command, and strings that either
    represent possible objects or prepositions
    """
    length = len(token_list)
    # None for tuple list will indicate an absence of user input
    if length == 0:
        return "error", ["No user input"]
    action = "unknown"
    object_preposition_list = []
    index = 0
    sentence_part = ""
    # Checks if first token is in list of allowable actions,
    # If not it could still indicate the user just gave direction of movement
    if token_list[0] in all_available_actions:
        action = token_list[0]
        index = 1
    # Loop through tokens to make list of possible objects and prepositions
    for word in token_list[index:]:
        if word in prepositions:
            # Upon reaching a preposition, preceding string considered
            # potential object
            if sentence_part != "":
                object_preposition_list.append(sentence_part.strip())
            # Append preposition
            object_preposition_list.append(word)
            sentence_part = ""
        else:
            sentence_part += word + " "
    if sentence_part != "":
        object_preposition_list.append(sentence_part.strip())
    return action, object_preposition_list


def parser(input, gamestate):
    """
    Parser that splits user input into an action and sets of strings
    then determines how to change game-state based on the action
    """
    token_list = tokenize(pre_process_commands(input))
    action, str_list = logic_splitter(token_list)
    if action == "error":
        return str_list[0]
    # Sends to helper that deals with actions that don't affect gamestate
    elif action in non_interactive_actions:
        return non_interactive_command_handler(action, gamestate)
    else:
        return interactive_command_handler(action, str_list, gamestate)


def non_interactive_command_handler(command, gamestate):
    """
    Helper function that handles all commands that don't affect gamestate
    """
    # Lists all items in player's inventory
    if command == "inventory":
        inv = gamestate.get_inventory()
        if not inv:
            return "You have nothing in your inventory"
        message = "The following items are in your inventory: "
        items = inv.keys()
        for item in items:
            message += item + ", "
        return message[:-2]
    # Returns vocabulary of usable actions
    elif command == "help":
        return "The following is a list of allowed commands:\nHelp\nInventory\n" \
               "Take\nDrop\nLook\nLook At\nExamine\nGo\nUse\nOpen\nUnlock\nSavegame\nLoadgame\n" \
               "Certain synonyms such as \"Pick Up\" or \"Move\" will also work"
    # Saves current game-state to a file
    elif command == "savegame":
        return "Not functional yet, sorry for the inconvenience"
    # Loads gamestate from a file
    elif command == "loadgame":
        return "Not functional yet, sorry for the inconvenience"
    # Gives long description of current room
    elif command == "look":
        # returns long description of room
        current_room = gamestate.get_current_room()
        return current_room.get_name() + "\n" +\
            current_room.get_long_description() + "\n" +\
            current_room.get_doors_and_items_description()


def interactive_command_handler(action, str_list, gamestate):
    # Attempts to add item to inventory
    if len(str_list) > 0 and action in pickup_actions:
        return take_handler(gamestate, str_list[0])
    # Attempts to drop item in inventory
    elif len(str_list) > 0 and action in drop_actions:
        return drop_handler(gamestate, str_list[0])
    # Attempts to have the player consume the item
    elif len(str_list) > 0 and action in eat_actions:
        return eat_handler(gamestate, str_list[0])
    # Attempts to go through door specified by user
    elif len(str_list) > 0 and action in movement_actions:
        return movement_handler(gamestate, str_list[0], True)
    elif len(str_list) > 0 and action == "unknown":
        return movement_handler(gamestate, str_list[0], False)
    # Gives description of possible item in room or inventory
    elif len(str_list) > 0 and action in examine_actions:
        return examine_handler(gamestate, str_list[0])
    # Attempts to use an item on an object or open a door with object
    elif len(str_list) > 2 and str_list[1] in prepositions and \
            (action in use_actions or action in open_actions):
        return use_open_splitter(gamestate, action, str_list)
    elif len(str_list) > 2 and str_list[1] in prepositions and \
            action in combine_actions:
        return combine_handler(gamestate, str_list)
    elif len(str_list) > 0 and action in use_actions:
        return use_handler(str_list[0], None, gamestate)
    return "Sorry I don't understand how to do that"


def movement_handler(gamestate, direction, known_status):
    """
    Handler that processes and performs movement actions
    """
    doors = gamestate.get_current_room().get_doors()
    door_name_list = list(doors.keys())
    lower_door_name_list = []
    directions = []
    # Gets list of all available movement directions and doors in lower case
    for door in door_name_list:
        lower_door_name_list.append(door.lower())
        directions.append(doors[door].get_direction().lower())

    # If user entered a valid cardinal direction and it is unlocked, perform movement and return message
    if direction in directions:
        door = doors[door_name_list[directions.index(direction)]]
        if not door.get_lock_status():
            description = perform_movement(gamestate, door)
            return "You have moved through the " + direction + " door\n\n" + description
        return "This door is locked"

    # If user entered a valid door name and it is unlocked, perform movement and return message
    elif direction in lower_door_name_list:
        door = doors[door_name_list[lower_door_name_list.index(direction)]]
        if not door.get_lock_status():
            description = perform_movement(gamestate, door)
            return "You have moved through the " + direction + "\n\n" + description
        return "This door is locked"

    # If user has used a move command but indicated an invalid direction
    elif known_status:
        return "You cannot move in that direction"

    # If user has not entered a valid command and not entered a movement direction
    return "I don't know how to " + direction


def perform_movement(gamestate, door):
    """
    Moves the player through the indicated door and changes the current
    room the player is in
    """
    new_room = door.get_destination()
    gamestate.set_current_room(new_room)
    new_room = gamestate.get_current_room()
    if new_room.get_visited():
        return new_room.get_name() + "\n" + new_room.get_short_description()\
               + "\n" + new_room.get_doors_and_items_description()
    new_room.set_visited()
    return new_room.get_name() + "\n" + new_room.get_long_description()\
        + "\n" + new_room.get_doors_and_items_description()


def examine_handler(gamestate, obj_name):
    """
    Returns the description of the object that the player wants to
    examine.
    """
    # return the description of object str_list[0]
    current_room = gamestate.get_current_room()

    # if it is an item in the current room
    item = current_room.get_item_by_name(obj_name)
    if item is not None:
        return item.get_description()
    else:
        # if it is a door in the current room
        door = current_room.get_door_by_name(obj_name)
        if door is not None:
            return door.get_description()
        else:
            # if it is an item in the player's inventory
            if obj_name in gamestate.get_inventory():
                item = gamestate.get_inventory()[obj_name]
                return item.get_description()
    # if the object is not found in the room or inventory
    return "That object isn't here"


def take_handler(gamestate, obj_name):
    """
    Takes and puts given object in inventory if it is
    in the current room and takeable.
    """
    # Add the item into inventory
    current_room = gamestate.get_current_room()
    item = current_room.get_item_by_name(obj_name)
    if item is not None:
        if item.is_takeable():
            gamestate.add_item_to_inventory(item.get_name(), item)
            current_room.remove_item(item)
            return item.get_name() + " is now in your inventory"

    # If the item was not in the room or could not be taken
    return "That object cannot be taken"


def drop_handler(gamestate, obj_name):
    """
    Tries to drop an item if it item exists in the inventory
    The item will be removed from the inventory and added to the current room
    """
    item = gamestate.get_item_by_name(obj_name)
    if item is not None:
        gamestate.get_current_room().add_item(item)
        gamestate.remove_item_from_inventory(obj_name)
        return "You have dropped " + obj_name + " from your inventory"

    # If the item is not in your inventory
    return "You do not have " + obj_name + " in your inventory"


def eat_handler(gamestate, obj_name):
    """
    Tries to consume the item if it is of food type and is in the
    inventory or current room
    """
    # if the item is in the current room
    current_room = gamestate.get_current_room()
    item = current_room.get_item_by_name(obj_name)
    if item is not None:
        if item.get_type() == "food":
            current_room.remove_item(item)
            return "You have consumed " + item.get_name()
        return "You can't eat that object"
    else:
        # if the item is in the player's inventory
        item = gamestate.get_item_by_name(obj_name)
        if item is not None:
            if item.get_type() == "food":
                gamestate.remove_item_from_inventory(obj_name)
                return "You have consumed " + item.get_name()
            return "You can't eat that object"
    return "No such object found"


def use_open_splitter(gamestate, action, str_list):
    """
    Handles input for both open actions and use actions.
    Note: use actions have a format of use x on y,
    while open actions have a format of open y with x
    Both formats are appropriate for doors, but use actions can be
    to have one object on another (potentially in future)
    """
    open_prepositions = ["with", "using"]
    use_prepositions = ["on", "upon"]
    cur_room = gamestate.get_current_room()

    # format for open actions is open y with/using x
    if action in open_actions and str_list[1] in open_prepositions:
        door = cur_room.get_door_by_name(str_list[0])
        key = gamestate.get_item_by_name(str_list[2])
        # Only call open_hander() if door is door, key is item with key property
        if door is not None and key is not None and key.get_type() == "key":
            return open_handler(key, door)
        elif door is None:
            return "There is no door with the name " + str_list[0] + " here"
        return "You do not have a " + str_list[2] + " in your inventory"

    # format for use actions is use x on/upon y
    elif str_list[1] in use_prepositions:
        item = gamestate.get_item_by_name(str_list[0])
        # Use commands might be done on either doors or other objects, so it
        # will search for both doors or items of that name in the room
        use_on_door = cur_room.get_door_by_name(str_list[2])
        use_on_item = cur_room.get_item_by_name(str_list[2])

        # Only call open_hander() if item is item with key property and the subject on
        # which it acts is a door
        if item is not None and use_on_door is not None and item.get_type() == "key":
            return open_handler(item, use_on_door)
        # If both item and subject on which it acts are items call use_handler()
        elif item is not None and use_on_item is not None:
            return use_handler(item, use_on_item)
        elif item is None:
            return "You do not have a " + str_list[0] + " in your inventory"
        return "There is nothing with the name" + str_list[2] + " here"

    return "I don't understand how to do that"


def open_handler(key, door):
    """
    Tries to unlock door using key
    param key: item object with key property
    param door: door object
    """
    # Open door only if key is appropriate for door and door is unlocked
    if door.get_key() == key.get_name() and door.get_lock_status():
        door.unlock_door()
        return "The door has been unlocked"
    # If key doesn't fit in door
    elif not door.get_key() == key.get_name():
        return "This key doesn't fit in this door"
    return "The door is already unlocked"


def use_handler(item, use_on_item, gamestate):
    """
    Will handle any use actions not involving doors
    """
    (message, hidden) = gamestate.get_use_info((item, use_on_item))
    if message is not None:
        if hidden is not None:
            cur_room = gamestate.get_current_room()
            hidden_object = cur_room.get_hidden_object_by_name(hidden)
            if hidden_object is not None:
                cur_room.remove_hidden(hidden_object)
                if isinstance(hidden_object, Item):
                    cur_room.add_item(hidden_object)
                if isinstance(hidden_object, Door):
                    cur_room.add_door(hidden_object)
        return random.choice(message)
    return "You cannot use " + item + " on " + use_on_item


def combine_handler(gamestate, str_list):
    if str_list[1] == "with":
        inv_1 = gamestate.get_item_by_name(str_list[0])
        inv_2 = gamestate.get_item_by_name(str_list[2])
        if inv_1 is None:
            return str_list[0] + " is not in your inventory"
        if inv_2 is None:
            return str_list[2] + " is not in your inventory"
        new_item = gamestate.get_combined_item_info((str_list[0], str_list[2]))
        if new_item is None:
            new_item = gamestate.get_combined_item_info((str_list[2], str_list[0]))
        if new_item is not None:
            gamestate.remove_item_from_inventory(str_list[0])
            gamestate.remove_item_from_inventory(str_list[2])
            gamestate.add_item_to_inventory(new_item.get_name(), new_item)
            return "You have combined " + str_list[0] + " and " + str_list[2] + \
                   " into " + new_item.get_name()
        return "You cannot combine those items"
    return "I don't understand how to do that"

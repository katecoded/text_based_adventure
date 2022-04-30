# from objects.game import Game

non_interactive_actions = ["inventory", "help", "look", "savegame", "loadgame"]
pickup_actions = ["take", "grab", "get", "pickup"]
movement_actions = ["go", "move", "travel"]
eat_actions = ["eat", "consume"]
examine_actions = ["lookat", "examine"]
other_actions = ["combine"]

all_available_actions = non_interactive_actions + pickup_actions + \
                        movement_actions + eat_actions + \
                        examine_actions + other_actions
prepositions = ["in", "at", "to", "with", "toward", "towards", "on", "into",
                "onto"]
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
    # Attempts to add item to inventory
    elif len(str_list) > 0 and action in pickup_actions:
        return take_handler(gamestate, str_list[0])
    # Attempts to go through door specified by user
    elif len(str_list) > 0 and action in movement_actions:
        return movement_handler(gamestate, str_list[0], True)
    elif len(str_list) > 0 and action == "unknown":
        return movement_handler(gamestate, str_list[0], False)
    # Gives description of possible item in room or inventory
    elif len(str_list) > 0 and action in examine_actions:
        return examine_handler(gamestate, str_list[0])
    # Attempts to combine two objects
    elif len(str_list) > 2 and action == "combine" and str_list[1] == "with":
        return "Attempts to combine " + str_list[0] + " with " + str_list[2]
    else:
        return "Sorry I don't understand how to do that"


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
        return "The following is a list of allowed commands:\nHelp\nInventory\nGo\n" \
               "Take\nLook\nLook At\nGo\nSavefile\nLoadfile\n" \
               "Certain synonyms such as \"Pick Up\" or \"Move\" will also work"
    # Saves current game-state to a file
    elif command == "savegame":
        return "Saves the current game state after asking for confirmation"
    # Loads gamestate from a file
    elif command == "loadgame":
        return "Loads last game save after asking for confirmation"
    # Gives long description of current room
    elif command == "look":
        # returns long description of room
        current_room = gamestate.get_current_room()
        return current_room.get_long_description()


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
    # If user entered a valid cardinal direction, perform movement and return message
    if direction in directions:
        description = perform_movement(gamestate, door_name_list[directions.index(direction)])
        return "You have moved through the " + direction + " door\n" + description
    # If user entered a valid door name, perform movement and return message
    elif direction in lower_door_name_list:
        description = perform_movement(gamestate, door_name_list[lower_door_name_list.index(direction)])
        return "You have moved through the " + direction + "\n" + description
    # If user has used a move command but indicated an invalid direction
    elif known_status:
        return "You cannot move in that direction"
    # If user has not entered a valid command and not entered a movement direction
    return "I don't know how to " + direction


def perform_movement(gamestate, door_name):
    """
    Moves the player through the indicated door and changes the current
    room the player is in
    """
    doors = gamestate.get_current_room().get_doors()
    new_room = doors[door_name].get_destination()
    gamestate.set_current_room(new_room)
    new_room = gamestate.get_current_room()
    if new_room.get_visited():
        return new_room.get_short_description() + "\n" + \
               new_room.get_doors_and_items_description()
    new_room.set_visited()
    return new_room.get_long_description() + "\n" + new_room.get_doors_and_items_description()


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
            return item.get_name() + " is now in your inventory"

    # If the item was not in the room or could not be taken
    return "That object cannot be taken"

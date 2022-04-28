from objects.game import Game

non_interactive_actions = ["inventory", "help", "look", "savegame", "loadgame"]
pickup_actions = ["take", "grab", "get", "pickup"]
movement_actions = ["go", "move"]
other_actions = ["lookat", "combine"]

all_available_actions = non_interactive_actions + pickup_actions + \
                        movement_actions + other_actions
prepositions = ["in", "at", "to", "with"]
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
    print(object_preposition_list)
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
        return "Attempts to take the object " + str_list[0]
    # Attempts to go through door specified by user
    elif len(str_list) > 0 and action in movement_actions:
        return movement_handler(gamestate, str_list[0], True)
    elif len(str_list) > 0 and action == "unknown":
        return movement_handler(gamestate, str_list[0], False)
    # Gives description of possible item in room
    elif len(str_list) > 0 and action == "lookat":
        return "Attempts to look at the object " + str_list[0]
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
        return "Gives long description of room"


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
        perform_movement(gamestate, door_name_list[directions.index(direction)])
        return "You have moved through the " + direction + " door"
    # If user entered a valid door name, perform movement and return message
    elif direction in lower_door_name_list:
        perform_movement(gamestate, door_name_list[lower_door_name_list.index(direction)])
        return "You have moved through the " + direction
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

# import string
non_interactive_actions = ["inventory", "help", "look", "savegame", "loadgame"]
pickup_actions = ["take", "grab", "get", "pickup"]
movement_actions = ["go", "move"]
other_actions = ["lookat", "combine"]

all_available_actions = non_interactive_actions + pickup_actions + \
                        movement_actions + other_actions
prepositions = ["in", "at", "to", "with"]
directions = ["north", "south", "east", "west"]  # up/down?


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
    for token in token_list:
        token = token.lower()
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

  
def temp_parser(input):
    """
    Placeholder for parser that splits user input into an action and sets of
    strings then determines how to change game-state based on the action
    """
    token_list = tokenize(pre_process_commands(input))
    action, str_list = logic_splitter(token_list)
    if action == "error":
        return str_list[0]
    # Sends to helper that deals with actions that don't affect gamestate
    elif action in non_interactive_actions:
        return non_interactive_command_handler(action)
    # Attempts to add item to inventory
    elif len(str_list) > 0 and action in pickup_actions:
        return "Attempts to take the object " + str_list[0]
    # Attempts to go through door specified by user
    elif len(str_list) > 0 and action in movement_actions:
        return "Attempts to go in the direction " + str_list[0]
    # Similar to above but should be updated to return different error
    elif len(str_list) > 0 and action == "unknown":
        return "Attempts to go in the direction " + str_list[0]
    # Gives description of possible item in room
    elif len(str_list) > 0 and action == "lookat":
        return "Attempts to look at the object " + str_list[0]
    # Attempts to combine two objects
    elif len(str_list) > 2 and action == "combine" and str_list[1] == "with":
        return "Attempts to combine " + str_list[0] + " with " + str_list[2]
    else:
        return "Sorry I don't understand how to do that"


def non_interactive_command_handler(command):
    """
    Helper function that handles all commands that don't affect gamestate
    """
    # Lists all items in player's inventory
    if command == "inventory":
        return "Displays inventory to user"
    # Returns vocabulary of usable actions
    elif command == "help":
        return "Displays list of standard actions to user"
    # Saves current game-state to a file
    elif command == "savegame":
        return "Saves the current game state after asking for confirmation"
    # Loads gamestate from a file
    elif command == "loadgame":
        return "Loads last game save after asking for confirmation"
    # Gives long description of current room
    elif command == "look":
        return "Gives long description of room"


def analyze_tokens(token_list):
    if len(token_list) == 0:
        return
    if token_list[0].lower() == "go":
        if len(token_list) > 1:
            pass
            # would call a function for navigating the player here
        else:
            print("Please provide a direction or adjacent room to go to.")

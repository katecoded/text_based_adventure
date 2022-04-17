# import string
available_actions = ["inventory", "help", "savegame", "loadgame", "combine",
                     "take", "grab", "get", "pick", "go", "move", "look"]
prepositions = ["in", "at", "to", "with"]
special_words = ["up"]


def tokenize(input):
    # Initially this will split string at spaces, may be refined after considering other strings
    token_list = input.split()
    for token in token_list:
        token = token.lower()
    return token_list


def logic_splitter(token_list):
    length = len(token_list)
    if length == 0:
        return None, None
    action = None
    object_preposition_list = []
    index = 0
    sentence_part = ()
    if token_list[0] in available_actions:
        action = token_list[0]
        index = 1
    for word in token_list[index:]:
        if word in prepositions or word in special_words:
            if sentence_part != ():
                object_preposition_list.append(sentence_part)
            sentence_part = (word,)
            object_preposition_list.append(sentence_part)
            sentence_part = ()
        else:
            sentence_part += (word,)
    if sentence_part != ():
        object_preposition_list.append(sentence_part)
    return action, object_preposition_list


def refine_input(input):
    token_list = tokenize(input)
    action, tuple_list = logic_splitter(token_list)
    if tuple_list is None:
        return "Error", ["No user input"]
    str_list = []
    for tuple in tuple_list:
        str = ""
        str += tuple[0]
        for word in tuple[1:]:
            str += " " + word
        str_list.append(str)
    if action is None:
        action = "go?"
    if action == "look" and str_list[0] == "at":
        str_list.pop(0)
        action = "lookat"
    if action == "pick" and str_list[0] == "up":
        str_list.pop(0)
        action = "take"
    return action, str_list


def temp_parser(input):
    action, str_list = refine_input(input)
    if action == "inventory":
        return "Displays inventory to user"
    elif action == "help":
        return "Displays list of standard actions to user"
    elif action == "savegame":
        return "Saves the current game state after asking for confirmation"
    elif action == "loadgame":
        return "Loads last game save after asking for confirmation"
    elif action == "look":
        return "Gives long description of room"
    elif len(str_list) > 0 and action == "lookat":
        return "Attempts to look at the object " + str_list[0]
    elif len(str_list) > 0 and action == "take" or action == "grab" or action == "get":
        return "Attempts to take the object " + str_list[0]
    elif len(str_list) > 0 and action == "go" or action == "move":
        return "Attempts to go in the direction " + str_list[0]
    # Similar to above but should return different error
    elif len(str_list) > 0 and action == "go?":
        return "Attempts to go in the direction " + str_list[0]
    elif len(str_list) > 2 and action == "combine" and str_list[1] == "with":
        return "Attempts to combine " + str_list[0] + " with " + str_list[2]
    else:
        return "Sorry I don't understand how to do that"


def analyze_tokens(token_list):
    if len(token_list) == 0:
        return
    if token_list[0].lower() == "go":
        if len(token_list) > 1:
            pass
            # would call a function for navigating the player here
        else:
            print("Please provide a direction or adjacent room to go to.")

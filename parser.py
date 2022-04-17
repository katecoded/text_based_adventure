# import string

non_interactive_actions = ["inventory", "help", "savegame", "loadgame"]
pickup_actions = ["take", "grab", "get"]
movement_actions = ["go", "move"]
#modal_actions = ["look"]
prepositions = ["in", "at"]


def tokenize(input):
    # Initially this will split string at spaces, may be refined after considering other strings
    token_list = input.split()
    for token in token_list:
        token = token.lower()
    return token_list


def input_parser(user_input):
    token_list = tokenize(user_input)
    length = len(token_list)
    if length == 0:
        return "Error", ""
    action = token_list[0]
    if action in non_interactive_actions:
        return action, ""
    if action == "look":
        if length > 1 and token_list[1] in prepositions:
            return "lookat", token_list[2]
        else:
            return action, ""
    if action in pickup_actions:
        if length > 1:
            return action, token_list[1]
        return "Error", "What am I picking up?"
    if action in movement_actions:
        if length > 1:
            return action, token_list[1]
        return "Error", "Where am I going?"
    if length > 1:
        return "Error", "I don't know how to " + action + " something"
    return "Error", "I don't know how to " + action


def analyze_tokens(token_list):
    if len(token_list) == 0:
        return
    if token_list[0].lower() == "go":
        if len(token_list) > 1:
            pass
            # would call a function for navigating the player here
        else:
            print("Please provide a direction or adjacent room to go to.")

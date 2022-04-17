# Actions that do not interact with elements
non_interactive_actions = ["inventory", "help", "savegame", "loadgame"]
# Different words for picking up something
pickup_actions = ["take", "grab", "get"]
# Different words for moving somewhere
movement_actions = ["go", "move"]
# Prepositions to be developed and expanded on
prepositions = ["in", "at"]


def tokenize(input):
    # Initially this will split string at spaces, may be refined after considering other strings
    token_list = input.split()
    for token in token_list:
        token = token.lower()
    return token_list


# Parser will analyze user input and return a tuple of action and subject to act on.
# Error is returned as an action anytime the input doesn't meet correct format
# Accompanying message should be output to user
def input_parser(user_input):
    token_list = tokenize(user_input)
    length = len(token_list)
    # If user doesn't input anything return an empty error
    if length == 0:
        return "Error", ""
    action = token_list[0]
    # Non-interactive actions don't have a subject to act on
    if action in non_interactive_actions:
        return action, ""
    # For now I made it so that if look at is not in correct format, just do a look instead
    if action == "look":
        if length > 2 and token_list[1] in prepositions:
            return "lookat", token_list[2]
        else:
            return action, ""
    if action in pickup_actions:
        if length > 1:
            return action, token_list[1]
        # Error returned if user doesn't input a subject, same for movement
        return "Error", "What am I picking up?"
    if action in movement_actions:
        if length > 1:
            return action, token_list[1]
        return "Error", "Where am I going?"
    # Errors returned if the user enters a nonsense action
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

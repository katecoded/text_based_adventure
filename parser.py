# import string

non_interactive_actions = ["inventory", "help", "savegame", "loadgame"]
interactive_actions = ["go", "take"]
modal_actions = ["look"]


def tokenize(input):
    # Initially this will split string at spaces, may be refined after considering other strings
    token_list = input.split()
    return token_list


def analyze_tokens(token_list):
    if len(token_list) == 0:
        return
    if token_list[0].lower() == "go":
        if len(token_list) > 1:
            pass
            # would call a function for navigating the player here
        else:
            print("Please provide a direction or adjacent room to go to.")

# import string

# Synonyms:
# ["go", "move", "travel"]
# ["take", "grab", "pick up"]
# ["examine", "look at"]

# these word lists can be added to
directions = ["north", "south", "east", "west"]
go_words = ["go", "move", "travel"]
take_words = ["take", "grab", "pick up"]
eat_words = ["eat", "consume"]
examine_words = ["examine", "look at"]

def_article_and_pronouns = ["the", "that", "this"]
prepositions = ["into", "onto", "toward", "towards", "to", "in", "on"]

# these are examples, can be changed/added to
room_names = ["kitchen", "foyer"]
door_names = ["oak door", "marble staircase"]
object_names = ["potato", "ghost"]


def tokenize(user_input):
    """
    Returns a list of tokens made from the user input
    :param user_input: the string statement given by the user
    :return: a list of terms that made up the user input
    """
    token_list = user_input.split()

    # we can rejoin tokens into one token for terms like "look at", etc.
    join_two_tokens(token_list, "pick", "up")
    join_two_tokens(token_list, "look", "at")
    join_two_tokens(token_list, "marble", "staircase")
    join_two_tokens(token_list, "oak", "door")

    return token_list


def join_two_tokens(token_list, word1, word2):
    """
    Joins two tokens into one, making a two-word term separated by a space
    :param token_list: the original list of tokens
    :param word1: the first word of the two-word term
    :param word2: the second word of the two-word term
    :return: none
    """
    start_idx = 0
    for token in token_list:
        if token.lower() == word1:
            tok_idx = token_list.index(word1, start_idx)
            if tok_idx < (len(token_list) - 1):
                if token_list[tok_idx + 1].lower() == word2:
                    token_list[tok_idx] = token_list[tok_idx] + " " + \
                                          token_list[tok_idx + 1]
                    del token_list[tok_idx + 1]
                    start_idx = tok_idx


def simplify_tokens(token_list):
    """
    Simplifies and reduces the token list by removing terms that can
    be ignored to make a simple command that can be analyzed
    :param token_list: the list of terms as tokens
    :return: none
    """
    for token in token_list:
        if token in def_article_and_pronouns or token in prepositions:
            del token_list[token_list.index(token)]


def analyze_tokens(token_list):
    """
    Analyzes the given token list and returns a command in a form of
    a tuple, with an action and object to perform the action on
    :param token_list: simplified list of tokens
    :return: command tuple: (action, object)
    """
    if len(token_list) == 0:
        return

    if token_list[0].lower() in go_words:
        if len(token_list) == 1:
            print("Please give a direction, exit, or adjacent room to go to.")

        else:
            for token in token_list:
                if token in room_names or token in door_names or \
                        token in directions:
                    return ("go", token)
                    # returns a command in the form
                    # of a tuple to move the player to the location

    elif token_list[0].lower() in directions:
        return ("go", token_list[0].lower())
        # returns a command in the form
        # of a tuple to move the player to the location

    elif token_list[0].lower() in room_names:
        return ("go", token_list[0].lower())
        # returns a command in the form
        # of a tuple to move the player to the location

    elif token_list[0].lower() in door_names:
        return ("go", token_list[0].lower())
        # returns a command in the form
        # of a tuple to move the player to the location

    elif token_list[0].lower() in take_words:
        if len(token_list) > 1:
            pass
            # would call a function for putting the object in inventory here
        else:
            print("Please provide an object to take.")

    elif token_list[0].lower() in examine_words:
        if len(token_list) > 1:
            pass
            # would call a function for examining the object here
        else:
            print("Please provide an object to examine.")
    elif token_list[0].lower() in eat_words:
        if len(token_list) > 1:
            pass
            # would call a function for eating the object here
        else:
            print("Please provide an object to eat.")


# print(analyze_tokens(["move", "to", "the", "foyer"]))

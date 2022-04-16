from load_rooms import load_rooms


class Game:
    pass


def main():
    """
    This function loads and runs the text_based_adventure game.
    """

    # load and store the room files
    rooms = load_rooms()

    # load the save (if there is one)

    # run the game until the user wants to stop/the game ends

import random
from objects.game import Game
from load_rooms import load_rooms
from tba_parser import parser
from use_and_combine_dicts import use_dict as use_dict, combine_dict as combine_dict


def set_up_game():
    """
    Sets up the starting information for the game in a Game
    object including the title, authors, starting location,
    all the rooms in the game, and an empty inventory.
    The rooms are loaded from external files.
    Returns a Game object.
    """
    title = "The Whimsical Castle"
    authors = ["Apoorva Magadi", "Fedor Titov",
               "Mason Stiller", "Katelyn Lindsey"]
    random.shuffle(authors)
    starting_location = "Courtyard"

    return Game(title, authors, load_rooms(), starting_location, {}, use_dict, combine_dict)


def introduction(game):
    """
    Outputs an introduction to the game including the title,
    authors, and a description of the game.
    """
    print(game.get_title())
    print("A text-based adventure game by ", end="")
    print(*game.get_authors(), sep=", ")
    print("\nYou wake up in a castle with no idea how you got there. "
          "Well, this is inconvenient.")
    print("(Use 'help' to see all available commands.)\n")


def starting_room(game):
    """
    Outputs a description of the starting room and sets that Room
    object as visited.
    """
    print(game.get_current_room().get_name())
    print(game.get_current_room().get_long_description())
    print(game.get_current_room().get_doors_and_items_description())
    game.get_current_room().set_visited()


def main():
    """
    Sets up and runs the text_based adventure game.
    """

    # first, set up the game by loading all rooms and storing
    # information such as the titles, authors and current location
    # in a Game object
    game = set_up_game()

    # output an introduction to the game
    introduction(game)

    # output the description/info for the starting room
    starting_room(game)

    # the game will keep running as long as this is True
    running = True

    while running:

        # get the command from the user
        user_command = input("\n> ")

        # if that command is to end the game, exit the game after
        # a confirmation
        if user_command.lower().strip() in\
                ["exit", "exit game", "end", "end game"]:
            # confirm the user's choice
            print("Warning - exiting does not save the game. "
                  "\nAre you sure? (Y/N)")
            choosing = True
            while choosing:
                choice = input("> ")
                if choice.lower().strip() in ["yes", "y", "1"]:
                    print("Thank you for playing!")
                    choosing = False
                    running = False
                elif choice.lower().strip() in ["no", "n", "0"]:
                    choosing = False
                else:
                    print("Not a valid choice. Try again.")
            continue

        # otherwise, pass that command on to the parser and output
        # the results
        print(parser(user_command, game))

        # if the diary is in the user's inventory, that triggers the
        # end of the game
        if "diary" in game.get_inventory():
            print("\nEpilogue"
                  "\nAn odd feeling comes over you as you hold the diary - "
                  "you feel strangely as if you have seen it before. And as "
                  "the peculiar sense of familiarity overtakes you, your "
                  "hands tremble as you open the book. "
                  "\nAll at once, a glow, gentle at first and then "
                  "overwhelmingly bright, shines from the diary. You have no "
                  "time to be afraid as the world seems to twist and tilt "
                  "sideways - and then, it rights itself. A strange sense of "
                  "calm flows through you, before you throw the book aside "
                  "with a jolt. This is your castle! No wonder it had "
                  "seemed so familiar. You had just been working on a "
                  "complicated spell this morning before..."
                  "\nYou smacked a hand to your forehead as memories of the "
                  "massive explosion of magic invade your mind, groaning at "
                  "the amount of repairs you'll have to do. "
                  "This is the last time you ever take advice from a "
                  "giant mushroom."
                  "\n\nThis concludes The Whimsical Castle."
                  "\nThank you for playing!")
            running = False


if __name__ == "__main__":
    main()

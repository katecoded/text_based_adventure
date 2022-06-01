import unittest
import os
import json
import random
from io import StringIO
from unittest import mock

from text_based_adventure import set_up_game, main, introduction, starting_room
from objects.room import Room
from objects.door import Door
from objects.item import Item


class TextBasedAdventureTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Changes the working directory to parent directory if
        needed.
        """
        # change the current working directory to the main directory if
        # tests is the current working directory
        if "tests" in os.getcwd():
            os.chdir("..")

        # get a list of all the room files in the game
        room_files = os.listdir("rooms")

        # make dictionary of dictionaries with room data (not actual
        # Room objects)
        cls.rooms = {}
        for file in room_files:
            with open("rooms/" + file) as room_json:
                # chop off leading "rooms_" and ending ".json" from name
                room_name = file[5:len(file) - 5]
                cls.rooms[room_name] = json.load(room_json)

    def test_set_up_game(self):
        """
        Validates that the set_up_game function returns a Game
        object that contains Room objects, which contains
        Door and Item objects.
        """
        game = set_up_game()
        rooms = game.get_all_rooms()

        # test that the game contains Room objects
        for room_name in rooms:
            self.assertIsInstance(rooms[room_name], Room)

            # test that the game contains Item objects
            items = rooms[room_name].get_items()
            for item_name in items:
                self.assertIsInstance(items[item_name], Item)

            # test that the game contains Door objects
            doors = rooms[room_name].get_doors()
            for door_name in doors:
                self.assertIsInstance(doors[door_name], Door)

    def test_introduction(self):
        """
        Validates that the introduction function outputs a String
        introduction to the game that includes the title and authors.
        """
        game = set_up_game()
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_out:
            introduction(game)
        intro_output = mock_out.getvalue()
        self.assertIn(game.get_title(), intro_output)
        self.assertIn(", ".join(game.get_authors()), intro_output)
        self.assertIsInstance(intro_output, str)

    def test_starting_room(self):
        """
        Validates that the starting_room function outputs a String
        containing the name and description of the starting room
        (Courtyard).
        """
        game = set_up_game()
        courtyard = self.rooms["courtyard"]
        expected_name_and_desc = courtyard["name"] + "\n" +\
            courtyard["long_description"] + "\n"

        with mock.patch('sys.stdout', new_callable=StringIO) as mock_out:
            starting_room(game)
        self.assertIn(expected_name_and_desc, mock_out.getvalue())

    def test_exit_game(self):
        """
        Validates that the words 'exit', 'exit game', 'end', and 'end game'
        all end the program.
        (This test validates that the main script exits and therefore does
        not require asserts.)
        """
        test_inputs = ["exit", "y", "exit game", "yes", "end", "1",
                       "end game", "Yes"]
        with mock.patch('sys.stdout', new_callable=StringIO):
            with mock.patch('builtins.input', side_effect=test_inputs):
                main()
                main()
                main()
                main()

    def test_examine_items_in_courtyard(self):
        """
        Validates that examining every item in the courtyard returns
        the correct descriptions.
        """
        courtyard = self.rooms["courtyard"]

        # create the test inputs and expected output
        test_inputs = []
        expected_output = []
        for item in courtyard["items"]:
            test_inputs.append(str(random.choice(["examine", "look at"])) +
                               " " + item)
            expected_output.append(courtyard["items"][item]["description"])
        test_inputs.append("exit")
        test_inputs.append("y")

        with mock.patch('sys.stdout', new_callable=StringIO) as mock_out:
            with mock.patch('builtins.input', side_effect=test_inputs):
                main()

        for expected in expected_output:
            self.assertIn(expected, mock_out.getvalue())

    def test_examine_doors_in_courtyard(self):
        """
        Validates that examining every door in the courtyard returns
        the correct descriptions.
        """
        courtyard = self.rooms["courtyard"]

        # create the test inputs and expected output
        test_inputs = []
        expected_output = []
        for door in courtyard["doors"]:
            test_inputs.append(str(random.choice(["examine", "look at"])) +
                               " " + door)
            expected_output.append(courtyard["doors"][door]["description"])
        test_inputs.append("exit")
        test_inputs.append("y")

        with mock.patch('sys.stdout', new_callable=StringIO) as mock_out:
            with mock.patch('builtins.input', side_effect=test_inputs):
                main()

        for expected in expected_output:
            self.assertIn(expected, mock_out.getvalue())

    def test_complete_game(self):
        """
        Validates that the game can be completed from start to finish.
        """
        test_inputs = ["take ivory key", "east", "take small telescope",
                       "east", "take iron key", "west", "unlock oak door "
                       "with ivory key", "west", "west", "examine pile of "
                       "rubble", "unlock trapdoor with iron key", "north",
                       "west", "examine weapon rack", "take tripod parts",
                       "north", "take red potion", "south", "east", "south",
                       "east", "east", "north", "north", "use red potion on "
                       "mass of mushrooms", "north", "combine small telescope "
                       "with tripod parts", "use mounted telescope on stone "
                       "pedestal", "west", "north", "take diary"]
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_out:
            with mock.patch('builtins.input', side_effect=test_inputs):
                main()

        expected_epilogue = "\nEpilogue" \
            "\nAn odd feeling comes over you as you hold the diary - " \
            "you feel strangely as if you have seen it before. And as " \
            "the peculiar sense of familiarity overtakes you, your " \
            "hands tremble as you open the book. " \
            "\nAll at once, a glow, gentle at first and then " \
            "overwhelmingly bright, shines from the diary. You have no " \
            "time to be afraid as the world seems to twist and tilt " \
            "sideways - and then, it rights itself. A strange sense of " \
            "calm flows through you, before you throw the book aside " \
            "with a jolt. This is your castle! No wonder it had " \
            "seemed so familiar. You had just been working on a " \
            "complicated spell this morning before..." \
            "\nYou smacked a hand to your forehead as memories of the " \
            "massive explosion of magic invade your mind, groaning at " \
            "the amount of repairs you'll have to do. " \
            "This is the last time you ever take advice from a " \
            "giant mushroom." \
            "\n\nThis concludes The Whimsical Castle." \
            "\nThank you for playing!"

        # assert epilogue is included in output (indicating end of game)
        self.assertIn(expected_epilogue, mock_out.getvalue())

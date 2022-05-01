import unittest
import os

from text_based_adventure import set_up_game
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

    def test_exit_game(self):
        """
        Validates that a few commands result in the expected output.
        """
        pass

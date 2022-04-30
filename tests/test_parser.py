import unittest
from unittest import TestCase
from parser import parser
from objects.game import Game
from objects.item import Item
from objects.room import Room
from objects.door import Door


class TestParser(TestCase):

    def setUp(self):
        """
        Sets up a test game instance
        """
        self.item_1 = Item("Crooked Candlestick", "A candlestick that paradoxically curves down"
                                                  "ward. How is this supposed to be used?", True)
        self.item_2 = Item("Sussy Coffee Cup", "A ceramic cup with the words \"Talk to me "
                                               "tomorrow\" emblazoned on the side. There is "
                                               "nothing suspicious about it...", True)
        self.item_3 = Item("Table", "It's a simple wooden table. There are items you make take "
                                    "on the table. No, you may not take the table.", False)
        self.item_4 = Item("flashlight",
                           "Ah, this flashlight might help in case you ever get"
                           "lost in some dark corner of this castle."
                           "It works a little too well though ... so bright...", True)
        self.item_5 = Item("hand mirror",
                           "Be careful with this. The last person who looked"
                           "into it for too long may or may not have gotten "
                           "sucked into it...", True)
        self.item_6 = Item("leather boot",
                           "Yup, just an old, dusty-looking leather boot.", True)

        self.door_1 = Door("One Door", "Rome", "North", False, "All doors lead to Rome")
        self.door_2 = Door("Two Door", "Rome", "East", False, "All doors lead to Rome")
        self.door_3 = Door("Red Door", "Rome", "South", False, "All doors lead to Rome")
        self.door_4 = Door("Blue Door", "Rome", "West", False, "All doors lead to Rome")
        self.room_1_door_dict = {self.door_1.get_name(): self.door_1,
                                 self.door_2.get_name(): self.door_2,
                                 self.door_3.get_name(): self.door_3,
                                 self.door_4.get_name(): self.door_4}
        self.room_1_item_dict = {self.item_1.get_name(): self.item_1,
                                 self.item_2.get_name(): self.item_2,
                                 self.item_3.get_name(): self.item_3,
                                 self.item_4.get_name(): self.item_4,
                                 self.item_5.get_name(): self.item_5,
                                 self.item_6.get_name(): self.item_6}
        self.room_1 = Room("Starting Room", "A Barren room with stuff on the table",
                           "A barren concrete room that serves as a starting point. In one of "
                           "the corners stands a simple wooden table with items of interest on "
                           "it. You may take the things on the table, but not the table itself.",
                           self.room_1_door_dict, self.room_1_item_dict)
        self.door_5 = Door("Rome Door", "Rome", "North", False, "All doors lead to Rome")
        self.door_6 = Door("Also Rome Door", "Rome", "East", False, "All doors lead to Rome")
        self.door_7 = Door("Still Rome Door", "Rome", "West", False, "All doors lead to Rome")
        self.door_8 = Door("Not Rome Door?!", "Starting Room", "South", False,
                           "You found the one door that doesn't lead to Rome. Unfortunately "
                           "it just goes back to the start")
        self.room_2_door_dict = {self.door_5.get_name(): self.door_5,
                                 self.door_6.get_name(): self.door_6,
                                 self.door_7.get_name(): self.door_7,
                                 self.door_8.get_name(): self.door_8}
        self.room_2 = Room("Rome", "Alan, please at details",
                           "To your surprise you have arrived at the ancient city of Rome. How a "
                           "whole city fits in one tiny room is a question that you cannot even "
                           "begin to answer. However, you very quickly realize that since this is "
                           "only a testing area you cannot interact with anything and that there "
                           "isn't even anything else here other than the concept of the city of "
                           "Rome. Shame.", self.room_2_door_dict, {})
        self.room_dict = {self.room_1.get_name(): self.room_1,
                          self.room_2.get_name(): self.room_2}
        self.game = Game("Test", "Great Old Ones", self.room_dict, "Starting Room", {})

    def test_take_command(self):
        message = parser("take flashlight", self.game)
        self.assertEqual(message, "flashlight is now in your inventory")

    def test_inventory_after_take_command(self):
        parser("take hand mirror", self.game)
        self.assertIn("hand mirror", self.game.get_inventory())

    def test_look_command(self):
        message = parser("look", self.game)
        self.assertEqual(message, self.game.get_current_room().get_long_description())

    def test_examine_command(self):
        message = parser("look at leather boot", self.game)
        item_desc = self.game.get_current_room().get_item_by_name("leather boot").get_description()
        self.assertEqual(message, item_desc)

    def test4(self):
        message = parser("combine gem with staff", self.game)
        self.assertEqual(message, "Attempts to combine gem with staff")

    def test7(self):
        message = parser("savegame", self.game)
        self.assertEqual(message, "Saves the current game state after asking for confirmation")

    def test8(self):
        message = parser("loadgame", self.game)
        self.assertEqual(message, "Loads last game save after asking for confirmation")

    def test_empty_user_input(self):
        """
        Test that empty user input is properly recognized
        """
        message = parser("", self.game)
        self.assertEqual(message, "No user input")

    def test_help_command(self):
        """
        Test that help command prints proper message
        """
        message = "The following is a list of allowed commands:\nHelp\nInventory\nGo\n" \
                  "Take\nLook\nLook At\nGo\nSavefile\nLoadfile\n" \
                  "Certain synonyms such as \"Pick Up\" or \"Move\" will also work"
        parser_output = parser("help", self.game)
        self.assertEqual(message, parser_output)

    def test_empty_inventory(self):
        """
        Tests that game properly returns message for empty inventory
        """
        message = parser("inventory", self.game)
        self.assertEqual(message, "You have nothing in your inventory")

    def test_one_item_inventory(self):
        """
        Tests that game properly returns inventory after one item is added
        """
        self.game.add_item_to_inventory(self.item_2.get_name(), self.item_2)
        message = parser("inventory", self.game)
        self.assertEqual(message, "The following items are in your inventory: Sussy Coffee Cup")

    def test_two_item_inventory(self):
        """
        Tests that game properly returns inventory after two items are added
        """
        self.game.add_item_to_inventory(self.item_1.get_name(), self.item_1)
        self.game.add_item_to_inventory(self.item_2.get_name(), self.item_2)
        message = parser("inventory", self.game)
        self.assertEqual(message, "The following items are in your inventory: "
                                  "Crooked Candlestick, Sussy Coffee Cup")

    def test_movement_message_direction(self):
        """
        Tests that game properly returns movement message given user tries to
        move using a cardinal direction
        """
        message = parser("move north", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(message, "You have moved through the north door\n" +
                         cur_room.get_long_description() + "\n" +
                         cur_room.get_doors_and_items_description())

    def test_movement_message_door(self):
        """
        Tests that game properly returns movement message given user tries to
        move using a door name
        """
        message = parser("go red door", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(message, "You have moved through the red door\n" +
                         cur_room.get_long_description() + "\n" +
                         cur_room.get_doors_and_items_description())

    def test_movement_direction(self):
        """
        Tests that game properly changes room given user tries to
        move using a cardinal direction
        """
        parser("move north", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(cur_room.get_name(), "Rome")

    def test_movement_door(self):
        """
        Tests that game properly changes room given user tries to
        move using a door name
        """
        parser("go red door", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(cur_room.get_name(), "Rome")

    def test_multiple_movement(self):
        """
        Tests that game properly changes room when given multiple
        movement commands
        """
        parser("go red door", self.game)
        parser("go south", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(cur_room.get_name(), "Starting Room")
        
    def test_multiple_movement_description(self):
        """
        Tests that game properly gives description for visited room
        after movement
        """
        parser("go red door", self.game)
        message = parser("go south", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(message, "You have moved through the south door\n" +
                         cur_room.get_short_description() + "\n" +
                         cur_room.get_doors_and_items_description())

    def test_movement_without_move_command(self):
        """
        Tests that game properly changes room when user doesn't use a
        command to move and just gives direction
        """
        parser("south", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(cur_room.get_name(), "Rome")

    def test_multiple_movement_without_move_command(self):
        """
        Tests that game properly changes room when user doesn't use a
        command to move and gives direction or door name
        """
        parser("south", self.game)
        parser("Not Rome Door?!", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(cur_room.get_name(), "Starting Room")

    def test_invalid_movement_direction(self):
        """
        Tests that game properly rejects movement in illegal directions
        """
        message = parser("go sideways", self.game)
        self.assertEqual(message, "You cannot move in that direction")

    def test_invalid_command(self):
        """
        Tests that game properly rejects incorrect commands after checking
        if user entered a direction of movement
        """
        message = parser("breathe ", self.game)
        self.assertEqual(message, "I don't know how to breathe")


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest import TestCase
from tba_parser import parser
from objects.game import Game
from objects.item import Item
from objects.room import Room
from objects.door import Door


class TestParser(TestCase):

    def setUp(self):
        """
        Sets up a test game instance
        """
        self.item_1 = Item("crooked candlestick", "A candlestick that paradoxically curves down"
                                                  "ward. How is this supposed to be used?", True)
        self.item_2 = Item("sussy coffee cup", "A ceramic cup with the words \"Talk to me "
                                               "tomorrow\" emblazoned on the side. There is "
                                               "nothing suspicious about it...", True)
        self.item_3 = Item("table", "It's a simple wooden table. There are items you make take "
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
        self.item_7 = Item("key", "A key for testing locks.", True, "key")
        self.item_8 = Item("fake key", "A fake key for testing locks.", True, "key")
        self.item_9 = Item("super table", "It's a special wooden table. Looking at it fills"
                                          "you with confidence. There are items you make take "
                                          "on the table. No, you may not take the table.", False)
        self.item_10 = Item("8-ball", "A magic 8-ball that tells the future.", True)
        self.door_1 = Door("one door", "Rome", "north", "", False, "All doors lead to Rome")
        self.door_2 = Door("two door", "Rome", "east", "key", True, "All doors lead to Rome")
        self.door_3 = Door("red door", "Rome", "south", "", False, "All doors lead to Rome")
        self.door_4 = Door("blue door", "Rome", "west", "", False, "All doors lead to Rome")
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
        self.hidden_dict = {self.item_9.get_name(): self.item_9}
        self.room_1 = Room("Starting Room", "A Barren room with stuff on the table",
                           "A barren concrete room that serves as a starting point. In one of "
                           "the corners stands a simple wooden table with items of interest on "
                           "it. You may take the things on the table, but not the table itself.",
                           self.room_1_door_dict, self.room_1_item_dict, self.hidden_dict)
        self.door_5 = Door("rome door", "Rome", "north", "", False, "All doors lead to Rome")
        self.door_6 = Door("also rome door", "Rome", "east", "", False, "All doors lead to Rome")
        self.door_7 = Door("still rome door", "Rome", "west", "", False, "All doors lead to Rome")
        self.door_8 = Door("not rome door?!", "Starting Room", "south", "", False,
                           "You found the one door that doesn't lead to Rome. Unfortunately "
                           "it just goes back to the start")
        self.room_2_door_dict = {self.door_5.get_name(): self.door_5,
                                 self.door_6.get_name(): self.door_6,
                                 self.door_7.get_name(): self.door_7,
                                 self.door_8.get_name(): self.door_8}
        self.room_2 = Room("Rome", "Alan, please add details",
                           "To your surprise you have arrived at the ancient city of Rome. How a "
                           "whole city fits in one tiny room is a question that you cannot even "
                           "begin to answer. However, you very quickly realize that since this is "
                           "only a testing area you cannot interact with anything and that there "
                           "isn't even anything else here other than the concept of the city of "
                           "Rome. Shame.", self.room_2_door_dict, {})
        self.room_dict = {self.room_1.get_name(): self.room_1,
                          self.room_2.get_name(): self.room_2}
        self.eight_ball_list = ["It is certain.", "It it's decidedly so.", "Without a doubt.",
                                "Yes definitely.", "You may rely on it.", "As I see it, yes.",
                                "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                                "Reply hazy, try again", "Ask again later.", "Better not tell you now.",
                                "Cannot predict now.", "Concentrate and ask again.",
                                "Don't count on it.", "My reply is no.", "My sources say no.",
                                "Outlook not so good.", "Very doubtful."]
        self.use_dict = {("flashlight", "table"): (["As you shine the flashlight upon the table, "
                                                    "you can't help but think it changed in some "
                                                    "small, imperceptible way"], "super table", False, False),
                         ("8-ball", None): (self.eight_ball_list, None, False, False)}
        self.item_99 = Item("flashlight in a boot", "It's a flashlight... stuck... into a... boot... "
                                                    "Yeaaah I really shouldn't be writing this after a "
                                                    "few drinks", True)
        self.combine_dict = {("flashlight", "leather boot"): self.item_99}
        self.game = Game("Test", "Great Old Ones", self.room_dict, "Starting Room", {}, self.use_dict,
                         self.combine_dict)
        self.game.get_current_room().set_visited()

    def test_take_command(self):
        message = parser("take flashlight", self.game)
        self.assertEqual(message, "flashlight is now in your inventory")

    def test_inventory_after_take_command(self):
        parser("take hand mirror", self.game)
        self.assertIn("hand mirror", self.game.get_inventory())

    def test_look_command(self):
        message = parser("look", self.game)
        self.assertEqual(message, self.game.get_current_room().get_name()
                         + "\n" + self.game.get_current_room().get_long_description()
                         + "\n" + self.game.get_current_room().get_doors_and_items_description())

    def test_examine_command(self):
        message = parser("look at leather boot", self.game)
        item_desc = self.game.get_current_room().get_item_by_name("leather boot").get_description()
        self.assertEqual(message, item_desc)

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
        message = "The following is a list of allowed commands:\nHelp\nInventory\n" \
                  "Take\nDrop\nLook\nLook At\nGo\nUse\nOpen\nUnlock\nCombine\nGive\n" \
                  "Eat\nTalk To\nSavegame\nLoadgame\n" \
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
        self.assertEqual(message, "The following items are in your inventory: sussy coffee cup")

    def test_two_item_inventory(self):
        """
        Tests that game properly returns inventory after two items are added
        """
        self.game.add_item_to_inventory(self.item_1.get_name(), self.item_1)
        self.game.add_item_to_inventory(self.item_2.get_name(), self.item_2)
        message = parser("inventory", self.game)
        self.assertEqual(message, "The following items are in your inventory: "
                                  "crooked candlestick, sussy coffee cup")

    def test_drop_item(self):
        """
        Tests that item is dropped properly after drop command
        """
        self.game.add_item_to_inventory(self.item_4.get_name(), self.item_4)
        message = parser("drop flashlight", self.game)
        self.assertEqual(message, "You have dropped " + self.item_4.get_name() +
                         " from your inventory")
        self.assertNotIn(self.item_4.get_name(), self.game.get_inventory())

    def test_movement_message_direction(self):
        """
        Tests that game properly returns movement message given user tries to
        move using a cardinal direction
        """
        message = parser("move north", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(message, "You have moved through the north door\n\n" +
                         cur_room.get_name() + "\n" +
                         cur_room.get_long_description() + "\n" +
                         cur_room.get_doors_and_items_description())

    def test_movement_message_door(self):
        """
        Tests that game properly returns movement message given user tries to
        move using a door name
        """
        message = parser("go red door", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(message, "You have moved through the red door\n\n" +
                         cur_room.get_name() + "\n" +
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
        self.assertEqual(message, "You have moved through the south door\n\n" +
                         cur_room.get_name() + "\n" +
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

    def test_move_locked_door(self):
        """
        Tests that game properly prevents you from moving throught locked
        door
        """
        message = parser("east", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(message, "This door is locked")
        self.assertEqual(cur_room.get_name(), "Starting Room")

    def test_invalid_movement_direction(self):
        """
        Tests that game properly rejects movement in illegal directions
        """
        message = parser("go sideways", self.game)
        self.assertEqual(message, "You cannot move in that direction")

    def test_unlock_door(self):
        """
        Tests that game properly unlocks door using key
        """
        self.game.add_item_to_inventory(self.item_7.get_name(), self.item_7)
        message = parser("open two door with key", self.game)
        self.assertEqual(message, "The door has been unlocked")
        self.assertFalse(self.door_2.get_lock_status())

    def test_move_through_unlocked_door(self):
        """
        Tests that game properly allows you to move through door only after it's
        unlocked
        """
        parser("east", self.game)
        self.game.add_item_to_inventory(self.item_7.get_name(), self.item_7)
        parser("use key on two door", self.game)
        parser("two door", self.game)
        cur_room = self.game.get_current_room()
        self.assertEqual(cur_room.get_name(), "Rome")

    def test_unlock_unlocked_door(self):
        """
        Tests that game properly rejects trying to open an open door
        """
        self.game.add_item_to_inventory(self.item_7.get_name(), self.item_7)
        parser("use key on two door", self.game)
        message = parser("unlock two door using key", self.game)
        self.assertEqual(message, "The door is already unlocked")
        self.assertFalse(self.door_2.get_lock_status())

    def test_wrong_key(self):
        """
        Tests that game properly rejects trying to open door with wrong key
        """
        self.game.add_item_to_inventory(self.item_8.get_name(), self.item_8)
        message = parser("utilize fake key upon two door", self.game)
        self.assertEqual(message, "This key doesn't fit in this door")
        self.assertTrue(self.door_2.get_lock_status())

    def test_missing_key(self):
        """
        Tests that game properly rejects opening lock with no key
        """
        message = parser("open two door with key", self.game)
        self.assertEqual(message, "You do not have a key in your inventory")
        self.assertTrue(self.door_2.get_lock_status())

    def test_unlock_wrong_door(self):
        """
        Tests that game properly rejects opening lock with wrong key
        """
        self.game.add_item_to_inventory(self.item_7.get_name(), self.item_7)
        message = parser("open one door with key", self.game)
        self.assertEqual(message, "This key doesn't fit in this door")
        self.assertFalse(self.door_1.get_lock_status())

    def test_unlock_non_existent_door(self):
        """
        Tests that game properly unlocks door using key
        """
        self.game.add_item_to_inventory(self.item_7.get_name(), self.item_7)
        message = parser("open three door with key", self.game)
        self.assertEqual(message, "There is no door with the name three door here")

    def illegal_use(self):
        """
        Tests that game properly rejects an improper use action
        At this stage it's anything other than opening door
        """
        self.game.add_item_to_inventory(self.item_7.get_name(), self.item_7)
        message = parser("use key on table", self.game)
        self.assertEqual(message, "You cannot use key + on table")

    def test_proper_use(self):
        """
        Tests that game properly rejects an improper use action
        At this stage it's anything other than opening door
        """
        self.game.add_item_to_inventory(self.item_4.get_name(), self.item_4)
        message = parser("use flashlight on table", self.game)
        self.assertEqual("As you shine the flashlight upon the table, you can't help but "
                         "think it changed in some small, imperceptible way", message)
        self.assertIn("super table", self.game.get_current_room().get_items())

    def test_multiple_message_use(self):
        self.game.add_item_to_inventory(self.item_10.get_name(), self.item_10)
        message = parser("use 8-ball", self.game)
        self.assertIn(message, self.eight_ball_list)

    def test_combine_test(self):
        self.game.add_item_to_inventory(self.item_4.get_name(), self.item_4)
        self.game.add_item_to_inventory(self.item_6.get_name(), self.item_6)
        message = parser("combine flashlight with leather boot", self.game)
        self.assertEqual("You have combined flashlight and leather boot into "
                         "flashlight in a boot", message)
        self.assertIn("flashlight in a boot", self.game.get_inventory())

    def test_combine_test_alt(self):
        self.game.add_item_to_inventory(self.item_4.get_name(), self.item_4)
        self.game.add_item_to_inventory(self.item_6.get_name(), self.item_6)
        message = parser("combine leather boot with flashlight", self.game)
        self.assertEqual("You have combined leather boot and flashlight into "
                         "flashlight in a boot", message)
        self.assertIn("flashlight in a boot", self.game.get_inventory())

    def test_combine_missing_item(self):
        self.game.add_item_to_inventory(self.item_4.get_name(), self.item_4)
        message = parser("combine flashlight with leather boot", self.game)
        self.assertEqual("leather boot is not in your inventory", message)

    def test_combine_missing_item_alt(self):
        self.game.add_item_to_inventory(self.item_6.get_name(), self.item_6)
        message = parser("combine flashlight with leather boot", self.game)
        self.assertEqual("flashlight is not in your inventory", message)

    def test_combine_invalid_items(self):
        self.game.add_item_to_inventory(self.item_4.get_name(), self.item_4)
        self.game.add_item_to_inventory(self.item_5.get_name(), self.item_5)
        message = parser("combine flashlight with hand mirror", self.game)
        self.assertEqual("You cannot combine those items", message)

    def test_invalid_command(self):
        """
        Tests that game properly rejects incorrect commands after checking
        if user entered a direction of movement
        """
        message = parser("breathe ", self.game)
        self.assertEqual(message, "I don't know how to breathe")


if __name__ == '__main__':
    unittest.main()

import unittest
from objects.game import Game
from objects.room import Room
from unittest.mock import Mock


class GameTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Creates Mocks for three items and two doors
        """
        cls.door1 = Mock()
        cls.door1.get_name.return_value = "brown door"
        cls.door2 = Mock()
        cls.door2.get_name.return_value = "blue door"
        cls.door_dict = {cls.door1.get_name(): cls.door1,
                         cls.door2.get_name(): cls.door2}

        cls.item1 = Mock()
        cls.item1.get_name.return_value = "gray pebble"
        cls.item2 = Mock()
        cls.item2.get_name.return_value = "loaf of bread"
        cls.item3 = Mock()
        cls.item3.get_name.return_value = "bouquet of roses"
        cls.item_dict = {cls.item1.get_name(): cls.item1,
                         cls.item2.get_name(): cls.item2}
        cls.item_list = [cls.item1, cls.item2]

    def test_get_title(self):
        """
        Tests for correct title being returned for a Game
        """
        title = "Game 1"
        authors = "author 1, author 2"
        foyer_room = Room("Foyer", "a small foyer",
                          "a small foyer that seems welcoming",
                          self.door_dict, self.item_dict)
        all_rooms = {"Foyer": foyer_room}
        inventory = self.item_list

        game1 = Game(title, authors, all_rooms, foyer_room, inventory)
        self.assertEqual(game1.get_title(), title)

    def test_get_authors(self):
        """
        Tests that correct authors are returned for a Game
        """
        title = "Game2"
        authors = "author 1, author 2"
        kitchen_room = Room("Kitchen", "a quaint kitchen",
                            "a kitchen full of pots and pans",
                            self.door_dict, self.item_dict)
        all_rooms = {"Kitchen": kitchen_room}
        inventory = self.item_list

        game2 = Game(title, authors, all_rooms, kitchen_room, inventory)
        self.assertEqual(game2.get_authors(), authors)

    def test_get_all_rooms(self):
        """
        Tests that the dictionary of all rooms is correctly returned
        """
        title = "Game2"
        authors = "author 1, author 2"
        kitchen_room = Room("Kitchen", "a quaint kitchen",
                            "a kitchen full of pots and pans",
                            self.door_dict, self.item_dict)
        bathroom = Room("Bathroom", "it's quite luxurious for a bathroom",
                        "a bathroom where jewels come out of the faucets...",
                        self.door_dict, self.item_list)
        all_rooms = {"Kitchen": kitchen_room,
                     "Bathroom": bathroom}
        inventory = self.item_list

        game2 = Game(title, authors, all_rooms, kitchen_room, inventory)
        self.assertEqual(game2.get_all_rooms(), all_rooms)

    def test_get_current_room(self):
        """
        Tests that player's current room is correctly returned
        """
        title = "Game3"
        authors = "author 1, author 2"
        kitchen_room = Room("Kitchen", "a quaint kitchen",
                            "a kitchen full of pots and pans",
                            self.door_dict, self.item_dict)
        bathroom = Room("Bathroom", "it's quite luxurious for a bathroom",
                        "a bathroom where jewels come out of the faucets...",
                        self.door_dict, self.item_list)
        all_rooms = {"Kitchen": kitchen_room,
                     "Bathroom": bathroom}
        inventory = self.item_list

        game3 = Game(title, authors, all_rooms, kitchen_room, inventory)
        self.assertEqual(game3.get_all_rooms(), all_rooms)

    def test_get_inventory(self):
        """
        Tests that player's current inventory is correctly returned
        """
        title = "Game3"
        authors = "author 1, author 2"
        kitchen_room = Room("Kitchen", "a quaint kitchen",
                            "a kitchen full of pots and pans",
                            self.door_dict, self.item_dict)
        bathroom = Room("Bathroom", "it's quite luxurious for a bathroom",
                        "a bathroom where jewels come out of the faucets...",
                        self.door_dict, self.item_list)
        all_rooms = {"Kitchen": kitchen_room,
                     "Bathroom": bathroom}
        inventory = self.item_list

        game3 = Game(title, authors, all_rooms, kitchen_room, inventory)
        self.assertEqual(game3.get_inventory(), inventory)

    def test_set_current_room(self):
        """
        Tests that player's new current room is correctly updated
        """
        title = "Game3"
        authors = "author 1, author 2"
        kitchen_room = Room("Kitchen", "a quaint kitchen",
                            "a kitchen full of pots and pans",
                            self.door_dict, self.item_dict)
        bathroom = Room("Bathroom", "it's quite luxurious for a bathroom",
                        "a bathroom where jewels come out of the faucets...",
                        self.door_dict, self.item_list)
        all_rooms = {"Kitchen": kitchen_room,
                     "Bathroom": bathroom}
        inventory = self.item_list

        game3 = Game(title, authors, all_rooms, kitchen_room, inventory)
        game3.set_current_room(bathroom)
        self.assertEqual(game3.get_current_room(), bathroom)

    def test_add_item_to_inventory(self):
        """
        Tests that player's inventory is correctly updated
        when an item is added to it
        """
        title = "Game3"
        authors = "author 1, author 2"
        kitchen_room = Room("Kitchen", "a quaint kitchen",
                            "a kitchen full of pots and pans",
                            self.door_dict, self.item_dict)
        bathroom = Room("Bathroom", "it's quite luxurious for a bathroom",
                        "a bathroom where jewels come out of the faucets...",
                        self.door_dict, self.item_list)
        all_rooms = {"Kitchen": kitchen_room,
                     "Bathroom": bathroom}
        inventory = self.item_list

        game3 = Game(title, authors, all_rooms, kitchen_room, inventory)
        game3.add_item_to_inventory(self.item3)
        self.assertIn(self.item3, game3.get_inventory())


if __name__ == '__main__':
    unittest.main()

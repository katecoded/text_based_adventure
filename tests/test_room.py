import unittest
from unittest.mock import Mock
from objects.room import Room


class RoomTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Sets up mocks for two items and two doors and their get_name
        methods in order to avoid these tests relying on the Item
        and Door classes.
        """
        cls.door = Mock()
        cls.door.get_name.return_value = "oak door"
        cls.door_2 = Mock()
        cls.door_2.get_name.return_value = "rustic door"
        cls.door_dict = {
            cls.door.get_name(): cls.door,
            cls.door_2.get_name(): cls.door_2
        }

        cls.item = Mock()
        cls.item.get_name.return_value = "silver key"
        cls.item_2 = Mock()
        cls.item_2.get_name.return_value = "purple mushroom"
        cls.item_dict = {
            cls.item.get_name(): cls.item,
            cls.item_2.get_name(): cls.item_2
        }

    def test_get_name(self):
        """
        Validates that the get_name method returns the correct
        String name.
        """
        name = "Foyer"
        short_description = "The marble room is full of ghosts."
        long_description = "The room is made entirely of marble. Strangely " \
                           "enough, this is not the oddest thing about " \
                           "this room, since it is also full of ghosts."
        doors = {}
        items = {}
        room = Room(name, short_description, long_description, doors, items)
        self.assertEqual(room.get_name(), name)

    def test_get_short_description(self):
        """
        Validates that the get_short_description method returns the
        correct String short_description.
        """
        name = "Dining Room"
        short_description = "There is a table in the center of this room" \
                            "...and it is full of small dragons."
        long_description = "A long oak table stretches across the room." \
                           "Dancing in the firelight, the forms of " \
                           "sleeping dragons fill both the table and the " \
                           "ceiling with strange shadows. A sense of dread " \
                           "hangs in the air."
        doors = {}
        items = {}
        room = Room(name, short_description, long_description, doors, items)
        self.assertEqual(room.get_short_description(), short_description)

    def test_get_long_description(self):
        """
        Validates that the get_long_description method returns the
        correct String long_description.
        """
        name = "Kitchen"
        short_description = "The floor and the walls are full of " \
                            "potatoes. How this happened is a mystery."
        long_description = "With the sparkling clean appliances and " \
                           "empty shelves, one would almost believe that " \
                           "this kitchen had never been touched...if it " \
                           "were not for the potatoes. The entire floor is " \
                           "covered in potatoes. And, if one looks closely " \
                           "enough, a hole in the wall reveals that the " \
                           "walls, too, are full of potatoes. How this " \
                           "could have happened is a mystery."
        doors = {}
        items = {}
        room = Room(name, short_description, long_description, doors, items)
        self.assertEqual(room.get_long_description(), long_description)

    def test_get_existing_door_by_name(self):
        """
        Validates that the get_door_by_name function returns the
        correct Door (mocked) object.
        """
        name = "Study"
        short_description = "The shelves are full of magic books."
        long_description = "Despite all expectations, the study appears " \
                           "to be what one would expect: a room " \
                           "overflowing with magic books, telescopes, " \
                           "cats, and dubious-looking potions."
        doors = self.door_dict
        items = self.item_dict
        room = Room(name, short_description, long_description, doors, items)
        self.assertEqual(
            room.get_door_by_name(self.door.get_name()),
            self.door
        )

    def test_get_non_existent_door_by_name(self):
        """
        Validates that the get_door_by_name function returns None
        when the Door is not in the Room.
        """
        name = "Frog Room"
        short_description = "There are frogs everywhere. Just..." \
                            "everywhere."
        long_description = "It's like a dream come true. On every " \
                           "wall - on every surface, in fact - there is " \
                           "a frog. It is the cutest thing in this " \
                           "entire mansion...even if it is extremely " \
                           "confusing."
        doors = {}
        items = {}
        room = Room(name, short_description, long_description, doors, items)
        self.assertIsNone(room.get_door_by_name("frogs"))

    def test_get_existing_item_by_name(self):
        """
        Validates that the get_item_by_name function returns the
        correct Item (mocked) object.
        """
        name = "Chair Hell"
        short_description = "The chairs are staring at you. " \
                            "You feel a sense of dread."
        long_description = "You are not entirely certain what you " \
                           "did to deserve this - perhaps you were " \
                           "a bit too critical of your office chairs " \
                           "in life - but in this afterlife, you seem " \
                           "to be surrounded by chairs. And not just " \
                           "any chairs - sentient, angry chairs. They " \
                           "look at you with clear malice in their eyes. " \
                           "You wonder if it's too late to repent."
        doors = self.door_dict
        items = self.item_dict
        room = Room(name, short_description, long_description, doors, items)
        self.assertEqual(
            room.get_item_by_name(self.item.get_name()),
            self.item
        )

    def test_get_non_existent_item_by_name(self):
        """
        Validates that the get_door_by_name function returns None
        when the Door is not in the Room.
        """
        name = "Sewing Room"
        short_description = "Fabric is spilling out of the shelves " \
                            "while a mouse is hard at work sewing a " \
                            "button on a sleeve."
        long_description = "The way the mouse on a nearby table " \
                           "scrutinizes your outfit makes you feel " \
                           "underdressed. Other than the overflowing " \
                           "fabric in the nearby shelves, most of the " \
                           "floor space is taken up by mannequins of " \
                           "various shapes and sizes. About a dozen mice " \
                           "are hard at work doing various repairs, from " \
                           "missing buttons to rips in seams. You wonder " \
                           "who these clothes are for."
        doors = {}
        items = {}
        room = Room(name, short_description, long_description, doors, items)
        self.assertIsNone(room.get_item_by_name("spoon"))


if __name__ == '__main__':
    unittest.main()

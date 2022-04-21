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
        cls.door.get_direction.return_value = "east"
        cls.door_2 = Mock()
        cls.door_2.get_name.return_value = "rustic door"
        cls.door_2.get_direction.return_value = "south"
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

    def test_get_doors_and_items_description(self):
        """
        Validates that when a Room has multiple Doors and multiple
        Items, the description with their names returns correctly.
        """
        name = "Plant Room"
        short_description = "The plant is going to eat you if " \
                            "you don't leave the room."
        long_description = "You seem to have woken up a large, " \
                           "carnivorous plant and it is very angry " \
                           "at you. It would be advisable to leave " \
                           "the room as soon as possible."
        doors = self.door_dict
        items = self.item_dict
        room = Room(name, short_description, long_description, doors, items)
        print(room.get_doors_and_items_description())

    def test_get_doors_and_items_description_2(self):
        """
        Validates that when a Room has multiple Doors and one Item,
        the description with their names returns correctly.
        """
        pass

    def test_get_doors_and_items_description_3(self):
        """
        Validates that when a Room has one Door and multiple Items,
        the description with their names returns correctly.
        """
        pass

    def test_get_doors_and_items_description_4(self):
        """
        Validates that when a Room has one Door and one Item,
        the description with their names returns correctly.
        """
        pass

    def test_get_doors_and_items_description_5(self):
        """
        Validates that when a Room has multiple Doors and no
        Items, the description with their names returns correctly.
        """
        pass

    def test_get_doors_and_items_description_6(self):
        """
        Validates that when a Room has one Door and no Items,
        the description with their names returns correctly.
        """
        pass

    def test_get_doors_and_items_description_7(self):
        """
        Validates that when a Room has no Doors and multiple
        Items, the description with their names returns correctly.
        """
        pass

    def test_get_doors_and_items_description_8(self):
        """
        Validates that when a Room has no Doors and one Item,
        the description with their names returns correctly.
        """
        pass

    def test_get_doors_and_items_description_9(self):
        """
        Validates that when a Room has no Doors or Items,
        the description of their names returns an empty string.
        Note: this should not be possible.
        """
        pass

    def test_get_visited_for_unvisited_room(self):
        """
        Validates that an unvisited Room's visited Boolean returns False.
        """
        name = "Underwater Courtyard"
        short_description = "A nearby child mermaid is poking you " \
                            "with a stick. You probably deserve it."
        long_description = "The courtyard, decorated with shimmering " \
                           "tiles and marble pillars, is so far " \
                           "underwater that you wonder if you will " \
                           "ever be able to leave. A group of dogs " \
                           "with fins and scales are playing nearby. " \
                           "You attempt to reconcile yourself with this " \
                           "reality as a mermaid child pokes you " \
                           "curiously with a stick."
        doors = {}
        items = {}
        room = Room(name, short_description, long_description, doors, items)
        self.assertFalse(room.get_visited())

    def test_set_visited(self):
        """
        Validates that a visited Room's visited Boolean is set
        correctly.
        """
        name = "Mushroom Forest"
        short_description = "Despite appearances, the mushroom " \
                            "monster before you seems quite content " \
                            "to be your friend."
        long_description = "Being greeted by a friendly mushroom " \
                           "monster is definitely the weirdest thing " \
                           "that has happened to you today. Well, other " \
                           "than being sent through a wormhole to a " \
                           "sentient mushroom forest. It is difficult " \
                           "to see anything past the mushroom's friendly " \
                           "(and very sharp) smile, but you suppose you " \
                           "could have worse friends."
        doors = {}
        items = {}
        room = Room(name, short_description, long_description, doors, items)
        room.set_visited()
        self.assertTrue(room.get_visited())

    def test_get_doors(self):
        """
        Validates that the get_doors method returns the
        expected Door objects.
        """
        name = "Yarn World"
        short_description = "Everything is made out of yarn - " \
                            "even you. You're unraveling at the " \
                            "thought."
        long_description = "A picturesque yarn landscape stretches " \
                           "for what seems like forever. It would " \
                           "be calming if you weren't also, somehow, " \
                           "made of yarn. You try your best to keep " \
                           "it together."
        doors = self.door_dict
        items = {}
        room = Room(name, short_description, long_description, doors, items)
        self.assertIn(self.door.get_name(), room.get_doors())
        self.assertIn(self.door_2.get_name(), room.get_doors())

    def test_get_items(self):
        """
        Validates that the get_items method returns the
        expected Item objects.
        """
        name = "Bees"
        short_description = "Bees bees bees bees bees"
        long_description = "Bees bees bees bees bees bees bees " \
                           "bees bees bees bees bees bees bees " \
                           "bees bees bees bees. Bees bees bees " \
                           "bees bees bees bees bees bees bees bees " \
                           "bees bees bees bees."
        doors = {}
        items = self.item_dict
        room = Room(name, short_description, long_description, doors, items)
        self.assertIn(self.item.get_name(), room.get_items())
        self.assertIn(self.item_2.get_name(), room.get_items())

    def test_get_existing_door_by_name(self):
        """
        Validates that the get_door_by_name method returns the
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
        Validates that the get_door_by_name method returns None
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
        Validates that the get_item_by_name method returns the
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
        Validates that the get_door_by_name method returns None
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

    def test_add_item(self):
        """
        Validates that adding an Item (mocked) object to a Room
        modifies the Room correctly and returns True.
        """
        name = "Poppy's Room"
        short_description = "The way that the doll's eyes glow " \
                            "fills you with dread. You are not sure " \
                            "why you decided to come back in here."
        long_description = "A sinister light fills the room, and you " \
                           "fill with dread as the doll on the table " \
                           "slowly opens its eyes. It is difficult to " \
                           "ignore the temptation to look at it, even " \
                           "though the gaudy wallpaper and large array " \
                           "of saws on the wall are a spectacle of their " \
                           "own. Entering this room may have been a " \
                           "mistake."
        doors = {}
        items = {}
        room = Room(name, short_description, long_description, doors, items)
        self.assertTrue(room.add_item(self.item))
        self.assertIn(self.item.get_name(), room.get_items())

    def test_add_existing_item(self):
        """
        Validates that adding an existing Item (mocked) object to a
        Room does not modify the Room and returns False.
        """
        pass

    def test_remove_item(self):
        """
        Validates that removing an existing Item (mocked) object from a
        Room modifies the Room correctly and returns True.
        """
        pass

    def test_remove_non_existent_item(self):
        """
        Validates that removing a non-existent Item (mocked) object
        from a Room does not modify the Room and returns False.
        """
        pass

    def test_add_door(self):
        """
        Validates that adding a Door (mocked) object to a Room
        modifies the Room correctly and returns True.
        """
        pass

    def test_add_existing_door(self):
        """
        Validates that adding an existing Door (mocked) object to a
        Room does not modify the Room and returns False.
        """
        pass

    def test_remove_door(self):
        """
        Validates that removing an existing Door (mocked) object from a
        Room modifies the Room correctly and returns True.
        """
        pass

    def test_remove_non_existent_door(self):
        """
        Validates that removing a non-existent Door (mocked) object
        from a Room does not modify the Room and returns False.
        """
        pass


if __name__ == '__main__':
    unittest.main()

import unittest
from objects.door import Door


class DoorTestCase(unittest.TestCase):

    def test_get_name(self):
        """
        Validates that the get_name method returns the correct
        String name.
        """
        name = "obsidian door"
        destination = "Dragon Room"
        direction = "west"
        key = ""
        locked = False
        description = "A sleek door made entirely out of obsidian."
        door = Door(name, destination, direction, key, locked, description)
        self.assertEqual(door.get_name(), name)

    def test_get_destination(self):
        """
        Validates that the get_destination method returns the correct
        String destination.
        """
        name = "obsidian door"
        destination = "Dragon Room"
        direction = "west"
        key = ""
        locked = False
        description = "A sleek door made entirely out of obsidian."
        door = Door(name, destination, direction, key, locked, description)
        self.assertEqual(door.get_destination(), destination)

    def test_get_direction(self):
        """
        Validates that the get_direction method returns the correct
        String direction.
        """
        name = "obsidian door"
        destination = "Dragon Room"
        direction = "west"
        key = ""
        locked = False
        description = "A sleek door made entirely out of obsidian."
        door = Door(name, destination, direction, key, locked, description)
        self.assertEqual(door.get_direction(), direction)

    def test_get_key(self):
        """
        Validates that the get_key method returns the correct
        String key name.
        """
        name = "obsidian door"
        destination = "Dragon Room"
        direction = "west"
        key = ""
        locked = False
        description = "A sleek door made entirely out of obsidian."
        door = Door(name, destination, direction, key, locked, description)
        self.assertEqual(door.get_key(), key)

    def test_get_lock_status_when_locked(self):
        """
        Validates that the get_lock_status method returns True
        when a Door is locked.
        """
        name = "obsidian door"
        destination = "Dragon Room"
        direction = "west"
        key = "pink passkey"
        locked = True
        description = "A sleek door made entirely out of obsidian."
        door = Door(name, destination, direction, key, locked, description)
        self.assertTrue(door.get_lock_status())

    def test_get_lock_status_when_unlocked(self):
        """
        Validates that the get_lock_status method returns False
        when a Door is unlocked.
        """
        name = "obsidian door"
        destination = "Dragon Room"
        direction = "west"
        key = "pink passkey"
        locked = False
        description = "A sleek door made entirely out of obsidian."
        door = Door(name, destination, direction, key, locked, description)
        self.assertFalse(door.get_lock_status())
        self.assertIsNotNone(door.get_lock_status())

    def test_get_description(self):
        """
        Validates that the get_description method returns the
        correct String description.
        """
        name = "obsidian door"
        destination = "Dragon Room"
        direction = "west"
        key = ""
        locked = False
        description = "A sleek door made entirely out of obsidian."
        door = Door(name, destination, direction, key, locked, description)
        self.assertEqual(door.get_description(), description)

    def test_unlock_door_with_locked_door(self):
        """
        Validates that the unlock_door method unlocks a locked
        Door.
        """
        name = "silver doorway"
        destination = "Frog Room"
        direction = "east"
        key = "golden trinket"
        locked = True
        description = "A doorway inlaid with silver. The mist renders it " \
                      "impassible when locked. You can see a swirled golden " \
                      "keyhole."
        door = Door(name, destination, direction, key, locked, description)
        self.assertTrue(door.get_lock_status())
        door.unlock_door()
        self.assertFalse(door.get_lock_status())
        self.assertIsNotNone(door.get_lock_status())

    def test_unlock_door_with_unlocked_door(self):
        """
        Validates that the unlock_door method locks an unlocked
        Door (functionality likely never to be used).
        """
        name = "silver doorway"
        destination = "Frog Room"
        direction = "east"
        key = "golden trinket"
        locked = False
        description = "A doorway inlaid with silver. The mist renders it " \
                      "impassible when locked. You can see a swirled golden " \
                      "keyhole."
        door = Door(name, destination, direction, key, locked, description)
        self.assertFalse(door.get_lock_status())
        self.assertIsNotNone(door.get_lock_status())
        door.unlock_door()
        self.assertTrue(door.get_lock_status())

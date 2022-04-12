import unittest
from objects.room import Room


class RoomTestCase(unittest.TestCase):

    def test_1(self):
        name = "Foyer"
        room = Room(name)
        self.assertEqual(room.get_name(), name)


if __name__ == '__main__':
    unittest.main()

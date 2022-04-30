import unittest
import json
import os

from objects.room import Room
from objects.item import Item
from objects.door import Door
from load_rooms import load_rooms


class LoadRoomsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Prepares a couple of test room JSON files to be used for the
        tests.
        """
        # change the current working directory to the main directory if
        # tests is the current working directory
        if "tests" in os.getcwd():
            os.chdir("..")

        # create the first JSON test file
        cls.test_file_data_1 = {
            "name": "Test File Bob's Room",
            "short_description": "This room belongs to Bob.",
            "long_description": "From all of the signs hanging around the "
                                "room, you can guess that this room belongs "
                                "to Bob.",
            "visited": False,
            "doors": {
                "broken door": {
                    "destination": "Unknown Room",
                    "direction": "west",
                    "key": "Unknown",
                    "description": "A door so broken that it is shattered "
                                   "to pieces in most places. It is unclear "
                                   "where it leads - not that you could "
                                   "open it anyway."
                },
                "hallway door": {
                    "destination": "Test File Hallway",
                    "direction": "north",
                    "key": "",
                    "description": "The door is covered in scratch "
                                   "marks. This is very concerning."
                }
            },
            "items": {
                "signs": {
                    "description": "There are numerous signs around the "
                                   "room. All of them say 'This room belongs "
                                   "to Bob.'",
                    "takeable": False,
                    "type": "decor"
                },
                "table": {
                    "description": "The wooden table is covered in signs.",
                    "takeable": False,
                    "type": "decor"
                }
            }
        }
        with open("rooms/room_test_1.json", "w+") as room_test_1:
            json.dump(cls.test_file_data_1, room_test_1)

        # create the second JSON test file
        cls.test_file_data_2 = {
            "name": "Test File Hallway",
            "short_description": "An empty hallway.",
            "long_description": "A spooky empty hallway.",
            "visited": True,
            "doors": {
                "squeaky door": {
                    "destination": "Test File Bob's Room",
                    "direction": "east",
                    "key": "",
                    "description": "A door so squeaky it could wake the "
                                   "dead"
                }
            },
            "items": {}
        }
        with open("rooms/room_test_2.json", "w+") as room_test_2:
            json.dump(cls.test_file_data_2, room_test_2)

    @classmethod
    def tearDownClass(cls):
        """
        Removes the test JSON files that were added.
        """
        os.remove("rooms/room_test_1.json")
        os.remove("rooms/room_test_2.json")

    def test_load_rooms_returns_rooms(self):
        """
        Verifies that load_rooms returns a dictionary of Room objects with
        the Room names (Strings) as keys.
        """
        room_dict = load_rooms()
        for room_name in room_dict.keys():
            self.assertIsInstance(room_name, str)
            self.assertIsInstance(room_dict[room_name], Room)

    def test_load_rooms_returns_items(self):
        """
        Verifies that each of the Rooms in the returned dictionary
        contain Item objects with their names (Strings) as keys.
        """
        room_dict = load_rooms()
        for room_name in room_dict.keys():
            items = room_dict[room_name].get_items()
            for item_name in items.keys():
                self.assertIsInstance(item_name, str)
                self.assertIsInstance(items[item_name], Item)

    def test_load_rooms_returns_doors(self):
        """
        Verifies that each of the Rooms in the returned dictionary
        contain Door objects with their names (Strings) as keys.
        """
        room_dict = load_rooms()
        for room_name in room_dict.keys():
            doors = room_dict[room_name].get_doors()
            for door_name in doors.keys():
                self.assertIsInstance(door_name, str)
                self.assertIsInstance(doors[door_name], Door)

import unittest
import json
import os
import jsonschema

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
        with open("rooms/room_test_1.json", "w") as room_test_1:
            json.dump(cls.test_file_data_1, room_test_1)

        # create the second JSON test file
        cls.test_file_data_2 = {
            "name": "Test File Hallway",
            "short_description": "An empty hallway.",
            "long_description": "A spooky empty hallway.",
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
        with open("rooms/room_test_2.json", "w") as room_test_2:
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

    def test_room_test_objects_exist(self):
        """
        Validates that the Test File Room objects are contained in the
        resulting returned dictionary.
        """
        room_dict = load_rooms()
        self.assertIn(self.test_file_data_1["name"], room_dict)
        self.assertIn(self.test_file_data_2["name"], room_dict)

    def test_room_1_properties_correct(self):
        """
        Validates that the first Test File Room object properties (created
        from test_file_data_1) contain the expected information.
        """
        room_dict = load_rooms()
        room = room_dict[self.test_file_data_1["name"]]
        self.assertEqual(room.get_name(), self.test_file_data_1["name"])
        self.assertEqual(room.get_short_description(),
                         self.test_file_data_1["short_description"])
        self.assertEqual(room.get_long_description(),
                         self.test_file_data_1["long_description"])
        self.assertFalse(room.get_visited())
        self.assertEqual(len(room.get_doors()),
                         len(self.test_file_data_1["doors"]))
        self.assertEqual(len(room.get_items()),
                         len(self.test_file_data_1["items"]))

    def test_room_2_properties_correct(self):
        """
        Validates that the second Test File Room object properties (created
        from test_file_data_2) contain the expected information.
        """
        room_dict = load_rooms()
        room = room_dict[self.test_file_data_2["name"]]
        self.assertEqual(room.get_name(), self.test_file_data_2["name"])
        self.assertEqual(room.get_short_description(),
                         self.test_file_data_2["short_description"])
        self.assertEqual(room.get_long_description(),
                         self.test_file_data_2["long_description"])
        self.assertFalse(room.get_visited())
        self.assertEqual(len(room.get_doors()),
                         len(self.test_file_data_2["doors"]))
        self.assertEqual(len(room.get_items()),
                         len(self.test_file_data_2["items"]))

    def test_room_1_item_data_correct(self):
        """
        Validates that the first Test File Room object's Item objects
        (created from test_file_data_1) contain the expected information.
        """
        room_dict = load_rooms()
        result_items = room_dict[self.test_file_data_1["name"]].get_items()
        expected_items = self.test_file_data_1["items"]

        for item_name in expected_items.keys():
            self.assertEqual(result_items[item_name].get_name(), item_name)
            self.assertEqual(result_items[item_name].get_description(),
                             expected_items[item_name]["description"])
            self.assertEqual(result_items[item_name].is_takeable(),
                             expected_items[item_name]["takeable"])

    def test_room_2_item_data_correct(self):
        """
        Validates that the second Test File Room object's Item objects
        (created from test_file_data_2) contain the expected information.
        """
        room_dict = load_rooms()
        result_items = room_dict[self.test_file_data_2["name"]].get_items()
        expected_items = self.test_file_data_2["items"]

        for item_name in expected_items.keys():
            self.assertEqual(result_items[item_name].get_name(), item_name)
            self.assertEqual(result_items[item_name].get_description(),
                             expected_items[item_name]["description"])
            self.assertEqual(result_items[item_name].is_takeable(),
                             expected_items[item_name]["takeable"])

    def test_room_1_door_data_correct(self):
        """
        Validates that the first Test File Room object's Door objects
        (created from test_file_data_1) contain the expected information.
        """
        room_dict = load_rooms()
        result_doors = room_dict[self.test_file_data_1["name"]].get_doors()
        expected_doors = self.test_file_data_1["doors"]

        for door_name in expected_doors.keys():
            self.assertEqual(result_doors[door_name].get_name(), door_name)
            self.assertEqual(result_doors[door_name].get_description(),
                             expected_doors[door_name]["description"])
            self.assertEqual(result_doors[door_name].get_direction(),
                             expected_doors[door_name]["direction"])
            self.assertEqual(result_doors[door_name].get_destination(),
                             expected_doors[door_name]["destination"])
            self.assertEqual(result_doors[door_name].get_key(),
                             expected_doors[door_name]["key"])
            self.assertEqual(result_doors[door_name].get_lock_status(),
                             bool(expected_doors[door_name]["key"]))

    def test_room_2_door_data_correct(self):
        """
        Validates that the second Test File Room object's Door objects
        (created from test_file_data_2) contain the expected information.
        """
        room_dict = load_rooms()
        result_doors = room_dict[self.test_file_data_2["name"]].get_doors()
        expected_doors = self.test_file_data_2["doors"]

        for door_name in expected_doors.keys():
            self.assertEqual(result_doors[door_name].get_name(), door_name)
            self.assertEqual(result_doors[door_name].get_description(),
                             expected_doors[door_name]["description"])
            self.assertEqual(result_doors[door_name].get_direction(),
                             expected_doors[door_name]["direction"])
            self.assertEqual(result_doors[door_name].get_destination(),
                             expected_doors[door_name]["destination"])
            self.assertEqual(result_doors[door_name].get_key(),
                             expected_doors[door_name]["key"])
            self.assertEqual(result_doors[door_name].get_lock_status(),
                             bool(expected_doors[door_name]["key"]))

    def test_json_validation_extra_room_property(self):
        """
        Validates that a room file with an extra room property
        causes a ValidationError.
        """
        # create room file with extra property
        room_data = {
            "name": "Frogs",
            "short_description": "There are frogs everywhere.",
            "long_description": "There are frogs everywhere.",
            "doors": {},
            "items": {},
            "frogs": "frogs"
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)

        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_name_property(self):
        """
        Validates that a room file with a missing name property
        causes a ValidationError.
        """
        # create room file with missing property
        room_data = {
            "short_description": "There are dogs everywhere.",
            "long_description": "There are dogs everywhere.",
            "doors": {},
            "items": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_short_description_property(self):
        """
        Validates that a room file with a missing short_description
        property causes a ValidationError.
        """
        # create room file with missing property
        room_data = {
            "name": "Wizards",
            "long_description": "You find yourself in a void. It would be "
                                "lonely if not for all of the angry wizards "
                                "surrounding you. You hope they don't turn "
                                "you into a frog.",
            "doors": {},
            "items": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_long_description_property(self):
        """
        Validates that a room file with a missing long_description
        property causes a ValidationError.
        """
        # create room file with missing property
        room_data = {
            "name": "Wizards",
            "short_description": "Despite the void surrounding you, you "
                                 "cannot help but be distracted by all of the "
                                 "wizards.",
            "doors": {},
            "items": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)

        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_doors_property(self):
        """
        Validates that a room file with a missing doors
        property causes a ValidationError.
        """
        # create room file with missing property
        room_data = {
            "name": "Wizards",
            "short_description": "Despite the void surrounding you, you "
                                 "cannot help but be distracted by all of the "
                                 "wizards.",
            "long_description": "You find yourself in a void. It would be "
                                "lonely if not for all of the angry wizards "
                                "surrounding you. You hope they don't turn "
                                "you into a frog.",
            "items": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_items_property(self):
        """
        Validates that a room file with a missing items
        property causes a ValidationError.
        """
        # create room file with missing property
        room_data = {
            "name": "Wizards",
            "short_description": "Despite the void surrounding you, you "
                                 "cannot help but be distracted by all of the "
                                 "wizards.",
            "long_description": "You find yourself in a void. It would be "
                                "lonely if not for all of the angry wizards "
                                "surrounding you. You hope they don't turn "
                                "you into a frog.",
            "doors": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_extra_item_property(self):
        """
        Validates that a room file with an extra item
        property causes a validation error.
        """
        # create room file with extra property
        room_data = {
            "name": "Blanket World",
            "short_description": "Blankets drape over every surface. You "
                                 "have never been more comfortable.",
            "long_description": "It is difficult to tell what this room "
                                "looks like due to the sheer number of "
                                "blankets decorating every surface and wall. "
                                "You have never been more comfortable.",
            "doors": {},
            "items": {
                "blankets": {
                    "description": "The blankets are soft. Most appear to "
                                   "be made out of wool.",
                    "takeable": False,
                    "type": "default",
                    "is_real": True
                }
            }
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_item_description_property(self):
        """
        Validates that a room file with a missing item description
        property causes a validation error.
        """
        # create room file with missing property
        room_data = {
            "name": "Blanket World",
            "short_description": "Blankets drape over every surface. You "
                                 "have never been more comfortable.",
            "long_description": "It is difficult to tell what this room "
                                "looks like due to the sheer number of "
                                "blankets decorating every surface and wall. "
                                "You have never been more comfortable.",
            "doors": {},
            "items": {
                "blankets": {
                    "takeable": False,
                    "type": "default"
                }
            }
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_item_takeable_property(self):
        """
        Validates that a room file with a missing item takeable
        property causes a validation error.
        """
        # create room file with missing property
        room_data = {
            "name": "Blanket World",
            "short_description": "Blankets drape over every surface. You "
                                 "have never been more comfortable.",
            "long_description": "It is difficult to tell what this room "
                                "looks like due to the sheer number of "
                                "blankets decorating every surface and wall. "
                                "You have never been more comfortable.",
            "doors": {},
            "items": {
                "blankets": {
                    "description": "The blankets are soft. Most appear to "
                                   "be made out of wool.",
                    "type": "default"
                }
            }
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_item_type_property(self):
        """
        Validates that a room file with a missing item type
        property causes a validation error.
        """
        # create room file with missing property
        room_data = {
            "name": "Blanket World",
            "short_description": "Blankets drape over every surface. You "
                                 "have never been more comfortable.",
            "long_description": "It is difficult to tell what this room "
                                "looks like due to the sheer number of "
                                "blankets decorating every surface and wall. "
                                "You have never been more comfortable.",
            "doors": {},
            "items": {
                "blankets": {
                    "description": "The blankets are soft. Most appear to "
                                   "be made out of wool.",
                    "takeable": False
                }
            }
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_extra_door_property(self):
        """
        Validates that a room file with an extra door
        property causes a validation error.
        """
        # create room file with extra property
        room_data = {
            "name": "Cord Catastrophy",
            "short_description": "The cord management in this room is a "
                                 "nightmare.",
            "long_description": "Futuristic computers line desks near the "
                                "wall. This would be cool if not for the "
                                "nightmare of cords twisting around the "
                                "floor. You shudder at the lack of cable "
                                "management.",
            "doors": {
                "copper door": {
                    "destination": "Test File Bob's Room",
                    "direction": "south",
                    "key": "",
                    "description": "Made entirely out of copper, the door "
                                   "is cool to the touch.",
                    "is_open": "yes"
                }
            },
            "items": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_door_destination_property(self):
        """
        Validates that a room file with a missing door destination
        property causes a validation error.
        """
        # create room file with missing property
        room_data = {
            "name": "Cord Catastrophy",
            "short_description": "The cord management in this room is a "
                                 "nightmare.",
            "long_description": "Futuristic computers line desks near the "
                                "wall. This would be cool if not for the "
                                "nightmare of cords twisting around the "
                                "floor. You shudder at the lack of cable "
                                "management.",
            "doors": {
                "copper door": {
                    "direction": "south",
                    "key": "",
                    "description": "Made entirely out of copper, the door "
                                   "is cool to the touch."
                }
            },
            "items": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_door_direction_property(self):
        """
        Validates that a room file with a missing door direction
        property causes a validation error.
        """
        # create room file with missing property
        room_data = {
            "name": "Cord Catastrophy",
            "short_description": "The cord management in this room is a "
                                 "nightmare.",
            "long_description": "Futuristic computers line desks near the "
                                "wall. This would be cool if not for the "
                                "nightmare of cords twisting around the "
                                "floor. You shudder at the lack of cable "
                                "management.",
            "doors": {
                "copper door": {
                    "destination": "Test File Bob's Room",
                    "key": "",
                    "description": "Made entirely out of copper, the door "
                                   "is cool to the touch."
                }
            },
            "items": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_door_key_property(self):
        """
        Validates that a room file with a missing door key
        property causes a validation error.
        """
        # create room file with missing property
        room_data = {
            "name": "Cord Catastrophy",
            "short_description": "The cord management in this room is a "
                                 "nightmare.",
            "long_description": "Futuristic computers line desks near the "
                                "wall. This would be cool if not for the "
                                "nightmare of cords twisting around the "
                                "floor. You shudder at the lack of cable "
                                "management.",
            "doors": {
                "copper door": {
                    "destination": "Test File Bob's Room",
                    "direction": "south",
                    "description": "Made entirely out of copper, the door "
                                   "is cool to the touch."
                }
            },
            "items": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

    def test_json_validation_missing_door_description_property(self):
        """
        Validates that a room file with a missing door description
        property causes a validation error.
        """
        # create room file with missing property
        room_data = {
            "name": "Cord Catastrophy",
            "short_description": "The cord management in this room is a "
                                 "nightmare.",
            "long_description": "Futuristic computers line desks near the "
                                "wall. This would be cool if not for the "
                                "nightmare of cords twisting around the "
                                "floor. You shudder at the lack of cable "
                                "management.",
            "doors": {
                "copper door": {
                    "destination": "Test File Bob's Room",
                    "direction": "south",
                    "key": ""
                }
            },
            "items": {}
        }
        with open("rooms/room_wrong.json", "w") as room_wrong:
            json.dump(room_data, room_wrong)
        with self.assertRaises(jsonschema.ValidationError):
            load_rooms()
        os.remove("rooms/room_wrong.json")

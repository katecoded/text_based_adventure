import unittest
from unittest import TestCase
from parser import temp_parser


class TestParser(TestCase):

    def test1(self):
        message = temp_parser("take key")
        self.assertEqual(message, "Attempts to take the object key")

    def test2(self):
        message = temp_parser("look")
        self.assertEqual(message, "Gives long description of room")

    def test3(self):
        message = temp_parser("look at sky")
        self.assertEqual(message, "Attempts to look at the object sky")

    def test4(self):
        message = temp_parser("")
        self.assertEqual(message, "No user input")

    def test5(self):
        message = temp_parser("move north")
        self.assertEqual(message, "Attempts to go in the direction north")

    def test6(self):
        message = temp_parser("combine gem with staff")
        self.assertEqual(message, "Attempts to combine gem with staff")

    def test7(self):
        message = temp_parser("grab the key")
        self.assertEqual(message, "Attempts to take the object the key")

    def test8(self):
        message = temp_parser("pick up the big blue ball")
        self.assertEqual(message, "Attempts to take the object the big blue ball")

    def test9(self):
        message = temp_parser("eat cake ")
        self.assertEqual(message, "Attempts to go in the direction eat cake")

    def test10(self):
        message = temp_parser("inventory")
        self.assertEqual(message, "Displays inventory to user")

    def test11(self):
        message = temp_parser("savegame")
        self.assertEqual(message, "Saves the current game state after asking for confirmation")

    def test12(self):
        message = temp_parser("help")
        self.assertEqual(message, "Displays list of standard actions to user")

    def test13(self):
        message = temp_parser("loadgame")
        self.assertEqual(message, "Loads last game save after asking for confirmation")


if __name__ == '__main__':
    unittest.main()

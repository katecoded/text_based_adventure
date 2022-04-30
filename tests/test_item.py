import unittest
from objects.item import Item


class ItemTestCase(unittest.TestCase):

    def test_get_name(self):
        """
        Validates that the get_name method returns the correct
        String name.
        """
        name = "silver key"
        description = "A silver key, tarnished with age."
        takeable = True
        type = "key"
        item = Item(name, description, takeable, type)
        self.assertEqual(item.get_name(), name)

    def test_get_description(self):
        """
        Validates that the get_description method returns the
        correct String description.
        """
        name = "wrinkled chair"
        description = "An old chair made of wrinkled and cracked " \
                      "leather. It gives off a musty odor."
        takeable = False
        type = "decor"
        item = Item(name, description, takeable, type)
        self.assertEqual(item.get_description(), description)

    def test_is_takeable_true(self):
        """
        Validates that is_takeable correctly returns True when
        takeable is True.
        """
        name = "fish tank"
        description = "Inside the tank, a goldfish looks back " \
                      "at you curiously. A nametag shows that " \
                      "its name is Steve."
        takeable = True
        type = "decor"
        item = Item(name, description, takeable, type)
        self.assertTrue(item.is_takeable())

    def test_is_takeable_false(self):
        """
        Validates that is_takeable correctly returns False when
        takeable is False.
        """
        name = "pineapple table"
        description = "The table is covered in drawings of " \
                      "pineapples. An odd assortment of fruit " \
                      "(also mostly pineapples) sits on top."
        takeable = False
        type = "decor"
        item = Item(name, description, takeable, type)
        self.assertFalse(item.is_takeable())


if __name__ == "__main__":
    unittest.main()

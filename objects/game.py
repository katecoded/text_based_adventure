
class Game:
    """
    Represents a Game instance of the text-based adventure game.
    The Game object has a title, authors, a dictionary of
    all the rooms within the game and keeps track of the player's
    current location and inventory.
    """

    def __init__(self, title, authors, all_rooms, current_room, inventory,
                 legal_use={}, combined_items={}):
        """
        Initializes a game with a title, authors, dictionary of rooms, and
        the player's current room and inventory.
        :param title: A String title for the Game
        :param authors: A String of the text-based adventure game's authors
        :param all_rooms: A dictionary holding all the rooms within the game
        :param current_room: A key corresponding to a room in the all_rooms
                        dictionary, representing the player's current position
        :param inventory: A dictionary that holds Item objects, representing
                        the player's inventory
        :param legal_use: A dictionary of tuples representing legal ways to use items
                        The format of the tuple is (message(s), hidden) where message
                        is what will be displayed to the user, hidden is the name of
                        the hidden item in the room to be revealed. The key is also a
                        tuple comprised of the name of the item in inventory to be used
                        and the item in room it is used on
        :param combined_items: A dictionary holding item objects, representing
                        items that can be obtained by combining two other items
                        Note that the key for these items is a tuple consisting of
                        the names of two items used to combine the item into one
        """
        self._title = title
        self._authors = authors
        self._all_rooms = all_rooms
        self._current_room = current_room
        self._inventory = inventory
        self._legal_use = legal_use
        self._combined_items = combined_items

    def get_title(self):
        """
        Returns the title of the Game
        :return: A String title
        """
        return self._title

    def get_authors(self):
        """
        Returns the authors of the Game
        :return: A String of the game's authors
        """
        return self._authors

    def get_all_rooms(self):
        """
        Returns all the rooms in the text-based adventure game
        :return: A Dictionary holding all the Rooms
        """
        return self._all_rooms

    def set_all_rooms(self, dictionary):
        """
        Sets the all rooms variable to a specified dictionary.
        """
        self._all_rooms = dictionary

    def get_current_room(self):
        """
        Returns the room the player is currently in
        :return: a Room object that the player is currently in
        """
        return self._all_rooms.get(self._current_room)

    def get_inventory(self):
        """
        Returns the player's inventory
        :return: a dictionary holding Items, representing the player's
                inventory
        """
        return self._inventory

    def reset_inventory(self):
        """
        Empties the player's current inventory.
        """
        self._inventory = {}

    def get_combined_items(self):
        """
        Returns dictionary of items obtained by combining
        :return: a dictionary holding Items, containing each item achieved
                by combining two other items
        """
        return self._combined_items

    def set_current_room(self, new_room_key):
        """
        Sets the player's current room to a new room
        :param new_room_key: Dictionary key for room in all_rooms
                        dictionary
        :return: none
        """
        self._current_room = new_room_key

    def get_item_by_name(self, item_key):
        """
        Returns the Item object from the inventory dictionary of Items
        with the given name if it exists. If it does not exist,
        None is returned
        :param item_key: A String name of item.
        """
        if item_key in self._inventory.keys():
            return self._inventory[item_key]
        else:
            return None

    def get_combined_item_info(self, item_key):
        """
        Returns the Item object from the dictionary of items obtained
        by combining two items, None if not found
        :param item_key: A tuple of two string that combine to obtain one item.
        """
        if item_key in self._combined_items.keys():
            return self._combined_items[item_key]
        else:
            return None

    def get_use_info(self, item_key):
        """
        Returns the info for legal cases of use command
        :param item_key: A tuple of two string representing used item and
                item it is used on respectively
        """
        if item_key in self._legal_use.keys():
            return self._legal_use[item_key]
        else:
            return None, None, None, None

    def add_item_to_inventory(self, new_item_key, new_item):
        """
        Adds a new Item to the player's inventory
        :param new_item_key: key for the item in dictionary
        :param new_item: Item object
        :return: none
        """
        self._inventory[new_item_key] = new_item

    def remove_item_from_inventory(self, item_key):
        """
        Removes an Item from the player's inventory
        :param item_key: key for the item in dictionary
        :return: none
        """
        self._inventory.pop(item_key)

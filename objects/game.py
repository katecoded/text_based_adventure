
class Game:
    """
    Represents a Game instance of the text-based adventure game.
    The Game object has a title, authors, a dictionary of
    all the rooms within the game and keeps track of the player's
    current location and inventory.
    """

    def __init__(self, title, authors, all_rooms, current_room, inventory):
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
        """
        self._title = title
        self._authors = authors
        self._all_rooms = all_rooms
        self._current_room = current_room
        self._inventory = inventory

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

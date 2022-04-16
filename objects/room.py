class Room:
    """
    Represents a Room in a text-based adventure game.
    A Room has a name, a short_description and a long_description,
    a visited Boolean for tracking if the room has been visited,
    a dictionary of Doors in the room, and a dictionary of Items in
    the room.
    """

    def __init__(self, name, short_description, long_description, doors,
                 items):
        """
        Initializes a Room with a name, a short_description,
        a long_description, a visited Boolean set to False,
        a dictionary of Doors, and a dictionary of Items.
        :name: A String name.
        :short_description: A String short description (1-2 sentences).
        :long_description: A String long description (a paragraph).
        :doors: A dictionary of Door objects.
        :items: A dictionary of Item objects.
        """
        self._name = name
        self._short_description = short_description
        self._long_description = long_description
        self._visited = False
        self._doors = doors
        self._items = items

    def get_name(self):
        """
        Returns the name of a Room.
        """
        return self._name

    def get_short_description(self):
        """
        Returns the short_description of a Room.
        """
        return self._short_description

    def get_long_description(self):
        """
        Returns the long_description of a Room.
        """
        return self._long_description

    def get_visited(self):
        """
        Returns the visited Boolean (whether the Room
        has been visited).
        """
        return self._visited

    def get_doors(self):
        """
        Returns the dictionary of Doors in the Room.
        """
        return self._doors

    def get_items(self):
        """
        Returns the dictionary of Items in the Room.
        """
        return self._items

    def get_door_by_name(self, name):
        """
        Returns the Door object from the Room's dictionary of Doors
        with the given name if it exists. If it does not exist,
        None is returned.
        :name: A String name.
        """
        if name in self._doors:
            return self._doors[name]
        return None

    def get_item_by_name(self, name):
        """
        Returns the Item object from the Room's dictionary of Items
        with the given name if it exists. If it does not exist,
        None is returned.
        :name: A String name.
        """
        if name in self._items:
            return self._items[name]
        return None

    def set_visited(self):
        """
        Sets the Rooms visited Boolean to True.
        """
        self._visited = True

    def add_item(self, item):
        """
        Adds the given item to the Room.
        Returns True if item is successfully added, False
        if the item is already in the Room.
        :item: An Item object.
        """
        pass

    def remove_item(self, item):
        """
        Removes the given item from the Room and returns True
        if it exists. If the item does not exist, False is
        returned.
        :item: An Item object.
        """
        pass

    def add_door(self, door):
        """
        Adds the given door to the Room.
        Returns True if door is successfully added, False
        if the door is already in the Room.
        :door: A Door object.
        """
        pass

    def remove_door(self, door):
        """
        Removes the given door from the Room and returns True
        if it exists. If the door does not exist, False is
        returned.
        :door: A Door object.
        """
        pass

class Room:
    """
    Represents a Room in a text-based adventure game.
    A Room has a name, a short_description and a long_description,
    a list of Doors in the room, and a list of Items in the room.
    """

    def __init__(self, name, short_description, long_description, doors,
                 items):
        """
        Initializes a Room with a name, a short_description,
        a long_description, a list of Doors, and a list of
        Items.
        :name: A String name.
        :short_description: A String short description (1-2 sentences).
        :long_description: A String long description (a paragraph).
        :doors: A dictionary of Door objects.
        :items: A dictionary of Item objects.
        """
        self._name = name
        self._short_description = short_description
        self._long_description = long_description
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

    def get_doors_description(self):
        """
        Returns a sentence description (String) of the
        names of the Doors in the Room.
        """
        pass

    def get_items_description(self):
        """
        Returns a sentence description (String) of the
        names of the Items in the Room.
        """
        pass

    def get_door_by_name(self, name):
        """
        Returns the Door object from the Room's list of Doors
        with the given name if it exists. If it does not exist,
        None is returned.
        :name: A String name.
        """
        if name in self._doors:
            return self._doors[name]
        return None

    def get_item_by_name(self, name):
        """
        Returns the Item object from the Room's list of Items
        with the given name if it exists. If it does not exist,
        None is returned.
        :name: A String name.
        """
        if name in self._items:
            return self._items[name]
        return None

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

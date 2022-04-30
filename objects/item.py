class Item:
    """
    Represents an Item in a text-based adventure game.
    An Item has a name, a description, and a Boolean for
    tracking if the Item can be picked up.
    """

    def __init__(self, name, description, takeable, type):
        """
        Initializes an Item with a name, a description,
        and a takeable Boolean.
        :name: A String name
        :description: A String description.
        :takeable: A Boolean representing if the Item can
            be taken (put in the player's inventory).
        """
        self._name = name
        self._description = description
        self._takeable = takeable
        self._type = type

    def get_name(self):
        """
        Returns the name of an Item.
        """
        return self._name

    def get_description(self):
        """
        Returns the description of an Item.
        """
        return self._description

    def is_takeable(self):
        """
        Returns if the Item is takeable (able to
        be put in the player's inventory).
        """
        return self._takeable

    def get_type(self):
        """
        Returns the Item type.
        """
        return self._type


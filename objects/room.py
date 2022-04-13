class Room:
    """
    Represents a Room in a text-based adventure game.
    """

    def __init__(self, name):
        """
        Initializes a Room with a name.
        """
        self._name = name

    def get_name(self):
        """
        Returns the name of a Room.
        """
        return self._name

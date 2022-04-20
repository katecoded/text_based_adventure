class Door:
    """
    Represents a door leading to a room in a text based adventure game.
    """

    def __init__(self, name, room, direction, key, short_desc, long_desc):
        """
        Initializes door object with a name, a room, a direction, a key status, and a lock status.
        """

        self._name = name
        self._room = room
        self._direction = direction
        self._key = key
        if self._key:
            self._locked = True
        else:
            self._locked = False
        self._short_desc = short_desc
        self._long_desc = long_desc

    def get_name(self):
        """returns the name of the door"""
        return self._name

    def get_room(self):
        """returns the name of the room the door leads to"""
        return self._room

    def get_direction(self):
        """returns the direction of the door in the current room the player is in"""
        return self._direction

    def get_key(self):
        """returns the name of the key or item needed to progress through the door"""
        return self._key

    def get_lock_status(self):
        """returns whether door is locked or not. True for locked, False for unlocked."""
        return self._locked

    def get_short_description(self):
        """returns short description string of the door"""
        return self._short_desc

    def get_long_description(self):
        """returns long description string of the door"""
        return self._long_desc

    def unlock_door(self):
        """
        switch lock status of door
        """
        if self._locked:
            self._locked = False

        if not self._locked:
            self._locked = True

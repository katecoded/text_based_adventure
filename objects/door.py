class Door:
    """
    Represents a door leading to a room in a text based adventure game.
    """

    def __init__(self, name, room, direction, key, short_desc, long_desc):
        """
        Initializes door object with a name, a room, a direction, a key status, and a lock status.
        """

        self.name = name
        self.room = room
        self.direction = direction
        self.key = key
        if self.key:
            self.locked = True
        else:
            self.locked = False
        self.short_desc = short_desc
        self.long_desc = long_desc

    def get_name(self):
        """returns the name of the door"""
        return self.name

    def get_room(self):
        """returns the name of the room the door leads to"""
        return self.room

    def get_direction(self):
        """returns the direction of the door in the current room the player is in"""
        return self.direction

    def get_key(self):
        """returns the name of the key or item needed to progress through the door"""
        return self.key

    def get_lock_status(self):
        """returns whether door is locked or not. True for locked, False for unlocked."""
        return self.locked

    def get_short_description(self):
        """returns short description string of the door"""
        return self.short_desc

    def get_long_description(self):
        """returns long description string of the door"""
        return self.long_desc

    def unlock_door(self):
        """
        switch lock status of door
        """
        self.locked = False

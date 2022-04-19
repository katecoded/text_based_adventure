class Game:
    """
    Represents the game-state for a text based adventure game
    The game class will have a title, authors,
    a dictionary of all the rooms in the game,
    a dictionary key corresponding to the room the player is currently in
    and a size 8 dictionary for all the items the player can hold
    """

    # Default starting inventory for a fresh game
    default_inventory = {
        "item_1": None,
        "item_2": None,
        "item_3": None,
        "item_4": None,
        "item_5": None,
        "item_6": None,
        "item_7": None,
        "item_8": None
    }

    def __init__(self, title, authors, room_list, cur_room, 
                 *, inventory=default_inventory):
        """
        Initializes a game object
        :title: The title of the game.
        :authors: Names of the devs and story writers
        :room_list: Dictionary of all rooms in the game
        :cur_room: Key value for room_list corresponding to 
        room player is currently in
        :inventory: A dictionary of items in player's inventory.
        By default, the inventory is empty(subject to change)
        """
        self.title = title
        self.authors = authors
        self.room_list = room_list
        self.cur_room = cur_room
        self.inventory = inventory

    def get_title(self):
        """
        Get title of game
        """
        return self.title

    def get_authors(self):
        """
        Get authors of game
        """
        return self.authors

    def get_room_list(self):
        """
        Get list of all rooms
        """
        return self.room_list

    def get_cur_room(self):
        """
        Get key for current room
        """
        return self.room_list[self.cur_room]

    def get_inventory(self):
        """
        Get list of all items in inventory
        """
        return self.inventory

    def set_room_list(self, new_room_list):
        """
        Change the list of all rooms
        Note: This might not be necessary as we 
        will likely change one room at a time
        """
        self.room_list = new_room_list

    def set_cur_room(self, room_key):
        """
        Changes the room the player is currently in by updating
        the key value corresponding to a room in the room dictionary
        """
        self.cur_room = room_key

    def set_inventory(self, new_inventory):
        """
        Change the list of all items in inventory
        Note: This might not be necessary as we 
        will likely change one item at a time
        """
        self.inventory = new_inventory

    def update_room(self, room_key, new_room):
        """
        Updates a singular room
        """
        self.room_list.update({room_key: new_room})

    def update_inventory(self, inventory_pos, item):
        """
        Updates a singular inventory item(None if emtpy)
        """
        self.inventory.update({inventory_pos: item})

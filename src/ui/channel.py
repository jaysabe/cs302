class Channel:
    __title = ""
    __active_users = []  # Replaces bookmarks
    __map = {}  # Channel lookup map

    def __init__(self, title: str, active_users: list[str]):
        self.__title = title
        self.__active_users = active_users
        self.__class__.__map[title.lower()] = self

    @classmethod
    def build(cls, data: dict) -> dict:
        """
        Builds a Channel object from a dictionary.

        Args:
            data (dict): A dictionary containing 'title', 'description', and 'topics'.

        Returns:
            Channel: A new Channel instance.
        """
        # TODO:
        return cls(data["title"], data["topics"])

    def get_key(self) -> str:
        """Returns the key for lookup, which is the lowercase version of the channel title."""
        return self.__title.lower()

    def get_title(self) -> str:
        """Returns the title of the channel."""
        return self.__title

    def get_active_users(self) -> list[str]:
        """Returns the list of users in the channel."""
        return self.__active_users

    def __str__(self) -> str:
        """Returns a string representation of the Channel."""
        return f"<Channel: {self.__title}>"

    def __iter__(self):
        """Allows iteration over the topics."""
        return iter(self.__active_users)

    def __contains__(self, user):
        """Checks if a user is in the channel."""
        return user in self.__active_users

    def add_topic(self, topic: str):
        """Adds a topic to the channel."""
        if topic not in self.__active_users:
            self.__active_users.append(topic)

    def remove_topic(self, user: str):
        """Removes a topic from the channel."""
        if user in self.__active_users:
            self.__active_users.remove(user)

    @classmethod
    def lookup(cls, title: str) -> 'Channel':
        """Looks up a channel by title."""
        return cls.__map.get(title.lower())

    @staticmethod
    def read_data():
        """Placeholder for reading data from a database or data structure."""
        pass  # TODO: Will be implemented later using a BST

    def to_dict(self) -> dict:
        """Converts the Channel to a dictionary."""
        return {
            "_id": self.get_key(),
            "title": self.__title,
            "users": self.__active_users,
        }

    def delete(self):
        """Placeholder for deleting the channel from a data structure."""
        del self.__class__.__map[self.get_key()]

    def add_to_database(self):
        """Placeholder for adding the channel to a data structure."""
        pass  # TODO: Will be implemented later using a BST

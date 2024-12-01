from ui.channel import Channel

class User:
    def __init__(self, username: str, user_id: int):
        self.username = username
        self.user_id = user_id
        self.__joined_channels = []  # list tracking topic channels

    def join_channel(self, channel_name: str):
        """
        Joins a channel if it exists and is not already joined.
        Args:
            channel_name (str): The name of the channel to join.
        """
        channel = Channel.lookup(channel_name)
        if not channel:
            print(f"Channel '{channel_name}' not found.")
            return

        if channel in self.__joined_channels:
            print(f"You are already in the channel '{channel.get_name()}'.")
        else:
            self.__joined_channels += channel_name
            print(f"Joined the channel '{channel.get_name()}'.")

    def leave_channel(self, channel_name: str):
        """
        Leaves a channel if the user is currently a member.

        Args:
            channel_name (str): The name of the channel to leave.
        """
        channel = Channel.lookup(channel_name)
        if not channel:
            print(f"Channel '{channel_name}' not found.")
            return

        if channel in self.__joined_channels:
            self.__joined_channels -= channel_name
            print(f"Left the channel '{channel.get_name()}'.")
        else:
            print(f"You are not a member of the channel '{channel_name}'.")

    def list_joined_channels(self):
        """
        Lists all channels the user has joined.
        """
        if not self.__joined_channels:
            print("You haven't joined any channels yet.")
        else:
            print("Joined Channels:")
            for channel in self.__joined_channels:
                print(f"- {channel.get_name()}")

    def get_joined_channels(self):
        """
        Returns a copy of the joined channels list for external use.
        """
        return [channel.get_name() for channel in self.__joined_channels]

    def __str__(self):
        return f"User(username='{self.username}', user_id={self.user_id})"
    
    def __iadd__(self, channel_name: str):
        """Overloaded += operator to join a channel."""
        print(f"Registered user {self.username} is joining '{channel_name}'...")
        self.join_channel(channel_name)
        return self

    def __isub__(self, channel_name: str):
        """Overloaded -= operator to leave a channel."""
        print(f"Registered user {self.username} left '{channel_name}'...")
        self.leave_channel(channel_name)
        return self
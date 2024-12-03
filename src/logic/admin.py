# Admin class
from .user import User
from ..ui.channel import Channel
from ..util import input_string, y_or_n, is_non_empty
import numpy as np

class Admin(User):
    def __init__(self, username:str, user_id: int, joined_channels: list):
        super().__init__(username, user_id, joined_channels)
        self.channel_stats = np.zeros((5,2))
        self.all_channels_log = {}
    def create_channel(self):
        """
        Prompts the admin to create a new channel with a name and optional description.
        """
        channel_name = input_string(
            prompt="Enter the name of the new channel: ",
            error="Channel name must be non-empty!",
            valid=is_non_empty
        )

        if Channel.lookup(channel_name):
            print(f"Channel '{channel_name}' already exists.")
            return

        description = input_string(
            prompt="Enter a description for the channel (optional): ",
            error="Description must be non-empty.",
            valid=lambda s: True  # Allow empty descriptions
        )

        new_channel = Channel(channel_name, description)
        print(f"Channel '{new_channel.get_title()}' created successfully.")

    def update_channel_stats(self, channel_name: str, user_count: int, msg_count: int):
        """
        Updates channel statistics for user count and message count.
        Args:
            channel_name (str): The name of the channel.
            user_count (int): Number of users in the channel.
            msg_count (int): Number of messages in the channel.
        """
        try:
            index = list(Channel._Channel__map.keys()).index(channel_name.lower())
            self.channel_stats[index, 0] = user_count
            self.channel_stats[index, 1] = msg_count
            print(f"Updated stats for '{channel_name}': Users={user_count}, Messages={msg_count}.")
        except ValueError:
            print(f"Channel '{channel_name}' not found in stats tracking.")

    def check_channel_stats(self):
        """
        Displays statistics of all channels including user breakdown by type.
        """
        print("Channel Statistics:")
        for index, (channel_name, channel) in enumerate(Channel._Channel__map.items()):
            user_count = len(channel.get_users())
            admin_count = sum(1 for user in channel.get_users() if isinstance(user, Admin))
            reg_user_count = user_count - admin_count

            print(f"Channel '{channel_name}': Total Users={user_count}, Admins={admin_count}, Registered Users={reg_user_count}")
            self.channel_stats[index, 0] = user_count
            self.channel_stats[index, 1] = 0  # Placeholder for messages (to be updated later)

    def remove_channel(self):
        """
        Prompts the admin to remove a channel if it exists.
        """
        channel_name = input_string(
            prompt="Enter the name of the channel to remove: ",
            error="Channel name must be non-empty!",
            valid=is_non_empty
        )

        try:
            channel = Channel.lookup(channel_name)
            del Channel._Channel__map[channel.get_key()]
            print(f"Channel '{channel_name}' removed successfully.")
        except KeyError:
            print(f"Channel '{channel_name}' not found.")

    def audit_user(self):
        """
        Pulls user info from BST (to be implemented) and offers to ban them.
        """
        username = input_string(
            prompt="Enter the username to audit: ",
            error="Username must be non-empty!",
            valid=is_non_empty
        )

        print(f"Auditing user '{username}'...")
        # Placeholder for BST interaction
        response = y_or_n(prompt="Ban this user? (yes/no): ")
        if response:
            print(f"User '{username}' has been banned.")
        else:
            print(f"User '{username}' was not banned.")

    def __str__(self):
        return f"Admin(username='{self.username}', user_id={self.user_id}')"
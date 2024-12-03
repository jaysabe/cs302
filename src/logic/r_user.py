# registered user class
from .user import User
from ..ui.channel import Channel

class RegisteredUser(User):
    def __init__(self, username: str, user_id: int, joined_channels: list = None):
        super().__init__(username, user_id, joined_channels or [])

    def post(self, msg: str, channel_name: str) -> None:
        """
        Posts a message to a channel the user has joined.

        Args:
        msg (str): The message to post.
        channel_name (str): The channel to post the message in.
        """
        # Find the channel object by its name (you may need to use lookup to get the actual channel)
        channel = Channel.lookup(channel_name)

        # Check if the channel exists and if the user has joined it
        if channel and channel in self.get_joined_channels():
            # Add the message to the channel's list of posts
            channel.add_post(msg)  # Ensure that the Channel class has an add_post() method
            print(f"[{self.username}] in [{channel.get_title()}]: {msg}")
        else:
            print(f"You must join the channel '{channel_name}' before posting.")


    def react(self, comment_id: int, reaction: str) -> None:
        """
        Reacts to a comment with the specified reaction.

        Args:
            comment_id (int): The ID of the comment to react to.
            reaction (str): The reaction to post. Accepted: "/happy", "/sad", "/tableflip"
        """
        valid_reactions = {"/happy": "😊", "/sad": "😢", "/tableflip": "(╯°□°）╯︵ ┻━┻"}
        if reaction in valid_reactions:
            print(f"[{self.username}] reacted to comment {comment_id} with {valid_reactions[reaction]}")
        else:
            print(f"Invalid reaction '{reaction}'. Use one of: /happy, /sad, /tableflip.")

    def post_question(self, question: str, channel_name: str) -> None:
        """
        Posts a question to a channel in the format "/q: <question>".

        Args:
            question (str): The question to post.
            channel_name (str): The channel to post the question in.
        """
        formatted_question = f"/q: {question}"
        self.post(formatted_question, channel_name)

    def __str__(self):
        """
        String representation of the RegisteredUser, including student status.
        """
        return f"RegisteredUser(username='{self.username}', user_id={self.user_id})"

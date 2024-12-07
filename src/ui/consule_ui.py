from ..logic.user import User
from ..logic.r_user import RegisteredUser
from ..logic.admin import Admin
from ..logic.bot import Bot
# from art import tprint

"""
Note that this consule is still under construction but core heirarchy is done
"""

class ConsoleUI:
    __all_users = []
    __all_channels = []

    # @staticmethod
    # def logo():
    #     tprint("Panels", font="random")
        
    def menu(self, title: str=" Main Menu ", options: list[str]=["\tl: print list of topic channels", "\tp: print users list"]):
        # self.logo()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"~~~~~~~~~~~~~~~~~~{title}~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for option in options:
            print(option)
        print(" x: exit program")
    
    @classmethod
    def init(cls):
        cls.__all_channels = []  # TODO: Replace with data from the BST
        cls.__all_users = []  # TODO: Load from storage
    
    @classmethod
    def print_users_info(cls):
        """Prints the list of all users registered on the platform."""
        if not cls.__all_users:
            print("No users registered yet.")
        else:
            for user in cls.__all_users:
                print(user)

    @classmethod
    def print_topic_channel(cls):
        """Prints the list of all available topic channels on the platform."""
        if not cls.__all_channels:
            print("No channels available.")
        else:
            for channel in cls.__all_channels:
                print(channel.get_title() if hasattr(channel, 'get_title') else channel)

    def main_loop(self):
        """The main game loop to handle user interaction."""
        self.init()  # Initialize data
        while True:
            self.menu()
            choice = input("Enter your choice (/help for commands): ").strip().lower()
            
            if choice == "l":
                self.print_topic_channel()
            elif choice == "p":
                self.print_users_info()
            elif choice == "x":
                print("Exiting program. Goodbye!")
                break
            elif choice == "/help":
                print("Available options: l, p, x, /help")
            else:
                print(f"Unknown command: {choice}")

if __name__ == '__main__':
    console = ConsoleUI()
    console.main_loop()
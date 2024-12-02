# main py 
from logic.user import User 
from logic.r_user import RegisteredUser
from logic.admin import Admin
from logic.bot import Bot
from art import *

class ConsoleUI:
    __all_users = []
    __all_channels = []

    @staticmethod
    def logo():
        tprint("Panels", font="random")
        
    def menu(self, title: str=" Main Menu ", options: list[str]=["\tl: print list of topic channels", "\t"]):
        self.logo()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"~~~~~~~~~~~~~~~~~~{title}~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for option in options:
            print(option)
        
        # print(" p: print users list")
        # print(" l: print list of topic channels")
        # print(" s: print messages for a selected topic channel")
        # print(" r: remove user from channel")
        print(" x: exit program")

        
    @classmethod
    def init(cls):
        cls.__all_channels, cls.__all_msg_logs #TODO: call to BST read_data() function
    
    
    @classmethod
    def print_users_info(cls):
        """
        Prints the list of all users registered on the platform.
        """
        if not cls.__all_users:
            print("No users registered yet.")
        else:
            for user in cls.__all_users:
                print(user)


    @classmethod
    def print_topic_channel(cls):
        """
        Prints the list of all available topic channels on the platform.
        """
        if not cls.__all_channels:
            print("No channels available.")
        else:
            for channel in cls.__all_channels:
                print(channel.get_name() if hasattr(channel, 'get_name') else channel)


    # def prompt_menu():
    #     choice = "/q"
    #     while choice != "/q":
    #         print("Please register to enter channel or type 'no' to cancel: ")


        """
        - I made consul-ui class for all inputs + calls to util file
        - Then updated / solidified permission methods for each core hierarchy class
        - updated bot class with other scripts
        
        
        
        Current class core:
            - User:
                - View topics
                - Join channel
                - Leave channel
        
            - Registered User
                - Register 
                - react to messages
                - post in channel
                - if student => ask a question script
            
            - Admin
                - Create a channel
                - Audit User (menu to interact with BST) (Requires BST check)
                - post in channel
            
            -Bot 
                - Post a Fun fact
                - run scripts function for each role
                - Notification of a new user + add it to the list
        
        ~~~~~~~~~~~~~~~~~~
        
        Stuff left to do:
            - BST implementation
            - glassbox tests
            - check roles for each user // add a general role_set(takes a dict) that then gets sent to switch statement scripts
        
        """
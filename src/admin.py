# Admin class
from user import User
import numpy as np
class Admin(User):
    def __init__(self):
        self.channel_stats = np.zeros((5,2))
        self.msg_log = {}
        # self.isAdmin = True
        # # set role for script bot
        # self.role = {"/create_channel": "Channel created.",
        # "/remove": "User removed.", self.isAdmin:True}
        
    def create_channel(self):
        pass

    def update_channel_stats(self, user_count, msg_count):
        self.channel_stats[0,0] = user_count
        self.channel_stats[0,1] = msg_count
        
    def audit_user(self, username):
        '''
        pulls userid from BST then bans them if answers "yes" 
        '''
        
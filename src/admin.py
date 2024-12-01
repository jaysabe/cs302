# Admin class
from user import User
import numpy as np
class Admin(User):
    def __init__(self):
        self.channel_stats = np.zeros((5,2))
        self.msg_log = {}
        
    def view_user_list(self):
        pass
    
    def update_channel_stats(self, user_count, msg_count):
        self.channel_stats[0,0] = user_count
        self.channel_stats[0,1] = msg_count
        
    def log_new_user(self, user_info:User)-> str:
        self.msg_log[user_info['username']] = user_info
        return "User not found." if not user_info else f"{user_info['username']} joined the server" 
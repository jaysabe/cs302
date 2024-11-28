import numpy as np
from datetime import datetime

class User:
    __username = ""
    __user_id = 0
    __channels = []
    
    def __init__(self, username: str, user_id: int):
        self.__username = username
        self.__user_id = user_id
        self._channels = []    
    
    def get_key(self):
        return self.__user_id
    
    def get_username(self):
        return self.__username.lower()
    
    def display_info(self):
        return f"User: {self.username}, ID: {self.user_id}"
    
    def view_curr_channels(self):
        return ["general", "tech", "sports", "music lounge"]
    
class RegisteredUser(User):
    def __init__(self, username, userid, is_student):
        super().__init__(username, userid)
        self.__is_student = is_student
        self._selected_channels = []
        
    def __iadd__(self, channel_name: str):
        # Adds user to channel, TODO += op makes this happen
        self._selected_channels.append(channel_name)    
    
    def set_flag(self, flag:bool):
        # sets to student user 
        self._is_student = flag
        
    
# ~~~~~~~~~~~~~~~~~~~~~~
# Bot Class (Derived Class)
# ~~~~~~~~~~~~~~~~~~~~~~
class Bot(User):
    def __init__(self, username: str, user_id: int):
        super().__init__(username, user_id)
        self._user_log = {}
    
    def post_fun_fact(self):
        return "Did you know that Honey never spoils??"
    
    def schedule_event(self, event_name: str, event_time: datetime):
        return {"name": event_name, "time": event_time}
    
    def log_new_user(self, user_info: dict):
        self._user_log[user_info["username"]] = user_info
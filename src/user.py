class User:
    __username = ""
    __user_id = 0
    __user_prefs = []
    
    def __init__(self, username: str, user_id: int):
        self.__username = username
        self.__user_id = user_id
        self.__user_prefs = []    
    
    def update_prefs(self):
        pass
    
    def get_key(self):
        return self.__user_id
    
    def get_username(self):
        return self.__username.lower()
    
    def display_info(self):
        return f"User: {self.username}, ID: {self.user_id}"
    
    def view_curr_channels(self):
        return ["general", "tech", "sports", "music lounge"]
    
    def join_channel(self, channel_name:str):
        raise PermissionError("Only registered users may enter channel.")
    
    def leave_channel(self, channel_name:str):
        raise PermissionError("Only registered users may enter channel.")
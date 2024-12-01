# registered user class
from user import User
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
        
    
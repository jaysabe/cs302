from user import User
import numpy as np
from datetime import datetime
import copy

class Bot(User):
    def __init__(self, username: str, user_id: int):
        super().__init__(username, user_id)
        self._user_log = {}
    
    '''Return a fun fact string.'''
    def post_fun_fact_script(self)-> str:
        return "Did you know that Honey never spoils??"
    
    '''Return a dictionary with event details'''
    def see_events_script(self, event_name: str, event_time: datetime)-> dict:
        return {"name": event_name, "time": event_time}
    
    def run_script(self, script: str)-> None:
        script = script.lower()
        match(script):
            case "/q":
                print('Exiting bot.')
                exit
            case "/fact":
                print(self.post_fun_fact_script())
            case "/v_nlog":
                print(self.view_new_user_script())
    
    '''TODO THIS WILL CALL A METHOD IN BST Log and return all users who joined the server this session.'''
    def view_new_user_script(self, user_info: dict) -> str:
        """
        Log and return a message showing all users who have joined during this session.

        Args:
            user_info (dict): A dictionary containing user details.

        Returns:
            str: A message listing all users who joined the server during this session or indicating that no new users have joined.
        """
        try:
            # Attempt to retrieve the 'username' key from user_info
            username = user_info.get('username')
            if username:
                # Log the new user if they are not already in the log
                if username not in self._user_log:
                    self._user_log[username] = copy.deepcopy(user_info)
        except AttributeError:
            return "Error: Invalid user_info provided."

        # Check if any users have joined
        if not self._user_log:
            return "No new users have joined the server this session."

        # Generate a list of all joined users
        all_users = ", ".join(self._user_log.keys())
        return f"Users who joined the server this session: {all_users}"

    '''Get a copy of the user log for future integration with BST.'''
    def get_user_log_copy(self) -> dict:
        """
        Returns a deep copy of the user log for future use.
        """
        return copy.deepcopy(self._user_log) 
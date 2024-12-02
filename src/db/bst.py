# BST logic present here plus dummy data location
from datetime import datetime
import copy
class BST:    
    '''TODO: THIS WILL CALL A METHOD IN BST Log and return all users who joined the server this session.'''
    def log_new_user_script(self, user_info: dict) -> str:
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
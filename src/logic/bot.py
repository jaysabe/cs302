from logic.user import User
import numpy as np
from datetime import datetime

class Bot(User):
    def __init__(self, username: str, user_id: int):
        super().__init__(username, user_id)
        self._command_stats = np.zeros((3, 2), dtype=object)
    
    def run_script(self, script: str):
        """
        Executes a script based on the user's role.

        Args:
            script (str): The command entered by the user)
        """
        script = script.lower()

        match script:
            # General commands for all users
            case "/q":
                print("Exiting bot.")
                exit()
            case "/fact":
                print(self.post_fun_fact_script())
            case "/today":
                print(self.post_date_n_time())    
            case "/chk_stats":
                print(self.print_command_stats())
        # Invalid command handler
            case _:
                print(f"Unknown command: {script}")
                
    
    def post_date_n_time(self) -> str:
        # Get the current date and time
        formatted_time = datetime.now().strftime("It's %B %d, %Y. It's %I:%M %p gamers! :)")
        
        # Return the formatted string
        return formatted_time
    
    '''Return a fun fact string.'''
    def post_fun_fact_script(self)-> str:
        return "Did you know that Honey never spoils??"
    
    def _update_command_stats(self, script: str):
        """Helper method to update the command statistics."""
        if script == "/q":
            self.command_stats[0, 0] += 1
            self.command_stats[0, 1] = datetime.now()
        elif script == "/fact":
            self.command_stats[1, 0] += 1
            self.command_stats[1, 1] = datetime.now()
        elif script == "/today":
            self.command_stats[2, 0] += 1
            self.command_stats[2, 1] = datetime.now()

    def print_command_stats(self):
        """Print the command statistics."""
        for i, command in enumerate(["/q", "/fact", "/today"]):
            count = self.command_stats[i, 0]
            last_accessed = self.command_stats[i, 1]
            print(f"Command: {command}, Used: {count} times, Last accessed: {last_accessed}")
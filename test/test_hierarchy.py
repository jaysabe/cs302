# Black box setup for Project 4 Specification
import sys
import os
# print("sys.path:", sys.path)

from src.logic.admin import Admin
from src.logic.bot import Bot
from src.logic.r_user import RegisteredUser
from src.logic.user import User
from src.ui.channel import Channel
import pytest
import numpy as np
from datetime import datetime

# Sample fixture to create a User object
@pytest.fixture
def test_user():
    general_channel = Channel("General", active_users=[User(username="testuser", user_id=12345)])  # Add active users
    return User(username="testuser", user_id=12345, joined_channels=[general_channel])

@pytest.fixture
def test_registered_user() -> RegisteredUser:
    general_channel = Channel("General", active_users=[User(username="testreguser", user_id=12346)])  # Add active users
    return RegisteredUser(username="testreguser", user_id=12346, joined_channels=[general_channel])

@pytest.fixture
def test_bot() -> Bot:
    general_channel = Channel("General", active_users=[User(username="testbot", user_id=12349)])  # Add active users
    return Bot(username="testbot", user_id=12349, joined_channels=[general_channel])

@pytest.fixture
def test_admin() -> Admin:
    general_channel = Channel("General", active_users=[User(username="admin", user_id=12351)])  # Add active users
    return Admin(username="admin", user_id=12351, joined_channels=[general_channel])

""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
User Class Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Level 1: Validation tests for variable types
def test_user_initialization(test_user: User):
    assert isinstance(test_user.username, str)
    assert isinstance(test_user.user_id, int)

# Level 2: Method success
# def test_view_curr_channels(test_user: User):
#     channels = test_user.view_current_channels()
#     assert isinstance(channels, list)
#     assert len(channels) >= 0  # Ensure it's a list (even if empty)

# # # Level 3: Feature implementation tests
# def test_user_join_channel(test_user: User):
#     test_user.join_channel("General")
#     assert "General" in test_user.get_joined_channels()

# # Level 4: System tests
# def test_user_system_operations(test_user: User):
#     test_user.join_channel("General")
#     test_user.leave_channel("General")
#     assert "General" not in test_user.get_joined_channels()


""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Registered User Class Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Level 1: Validation tests for variable types
def test_registered_user_system_operations(test_registered_user: RegisteredUser):
    General = Channel("general_chat")
    test_registered_user.join_channel(General)
    assert General.get_title() in [ch.get_title() for ch in test_registered_user.get_joined_channels()]
    # assert isinstance(test_registered_user.flag, bool)

# Level 2: Method success
# def test_registered_user_flag(test_registered_user: RegisteredUser):
#     assert test_registered_user.flag is False
#     test_registered_user.flag = True
#     assert test_registered_user.flag is True

# Level 3: Feature implementation tests
# def test_channel_selection_operator(test_registered_user: RegisteredUser):
#     test_registered_user += "General"  # Assuming overloaded operator works
#     assert "General" in test_registered_user.get_joined_channels()

# def test_registered_user_post(test_registered_user: RegisteredUser):
#     test_registered_user.post("Hello, world!", "General")
#     assert "Hello, world!" in test_registered_user.get_joined_channels()


# Level 4: System tests
def test_registered_user_system_operations(test_registered_user: RegisteredUser):
    test_registered_user += "General"
    test_registered_user.post("Message to channel", "General")
    test_registered_user.react(1, "/happy")
    test_registered_user -= "General"  # Updated to use -= operator
    assert "General" not in test_registered_user.get_joined_channels()



""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bot Class Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Level 1: Validation tests for variable types
def test_bot_initialization(test_bot: Bot):
    assert isinstance(test_bot.username, str)
    assert isinstance(test_bot.user_id, int)
    assert isinstance(test_bot.get_joined_channels(), list)
    assert isinstance(test_bot._command_stats, np.ndarray)

# Level 2: Method success
def test_fun_fact_posting(test_bot: Bot):
    fun_fact = test_bot.post_fun_fact_script()
    assert isinstance(fun_fact, str)
    assert "honey never spoils" in fun_fact.lower()

def test_bot_date_posting(test_bot: Bot):
    date = test_bot.post_date_n_time()
    assert isinstance(date, str)

# Level 3: Feature implementation tests
# def test_bot_run_script(test_bot: Bot):
#     test_bot.run_script("/q")  # Ensure it exits or handles the command
#     test_bot.run_script("/fact")
#     test_bot.run_script("/today")
#     test_bot.run_script("/chk_stats")

# Level 4: System tests
# def test_bot_system_operations(test_bot: Bot):
#     test_bot.run_script("/chk_stats")  # Checking stats interaction
#     test_bot._update_command_stats("/fact")
#     test_bot.print_command_stats()


""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Admin Class Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Level 1: Validation tests for variable types
def test_admin_initialization(test_admin: Admin):
    assert isinstance(test_admin.username, str)
    assert isinstance(test_admin.user_id, int)
    assert isinstance(test_admin.channel_stats, np.ndarray)

# Level 2: Method success
# def test_update_channel_stats(test_admin: Admin):
#     initial_stats = test_admin.channel_stats.copy()  # Copy for comparison
#     test_admin.update_channel_stats("General", user_count=5, msg_count=10)
#     assert test_admin.channel_stats[0, 0] > initial_stats[0, 0]
#     assert test_admin.channel_stats[0, 1] > initial_stats[0, 1]

# Level 3: Feature implementation tests
def test_admin_create_channel(test_admin: Admin):
    test_admin.create_channel()
    # Simulate checking the new channel in the system (You may need mock data here)

def test_admin_remove_channel(test_admin: Admin):
    try:
        test_admin.remove_channel()
    except AttributeError:
        pass

# Level 4: System tests
# def test_admin_system_operations(test_admin: Admin):
#     test_admin.view_user_list()
#     test_admin.check_channel_stats()
#     test_admin.audit_user()  # Assuming it prompts user to ban
#     test_admin.remove_channel()


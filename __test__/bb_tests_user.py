# Black box setup for Project 4 Specification
import pytest
import numpy as np
from datetime import datetime
from src.user import User, RegisteredUser, Bot, Admin

# Blackbox Tests
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
User Class Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

@pytest.fixture
def test_user_init():
    user = User("testuser", user_id=12345)
    assert user.username == "testuser"
    assert user.user_id == 12345
    
def test_view_curr_channels():
    user = User("testuser", user_id=12345)
    channels = user.view_current_channels()
    assert isinstance(channels, list)
    assert len(channels) > 0 # aka not empty or none

""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Registered User Class Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def test_registered_user_initialization():
    registered_user = RegisteredUser(username="testreguser", user_id=12346, flag=False)
    assert registered_user.username == "testreguser"
    assert registered_user.user_id == 12346
    assert registered_user.flag is False

def test_registered_user_flag():
    registered_user = RegisteredUser(username="teststudentuser", user_id=12347, flag=True)
    assert registered_user.flag is True

def test_channel_selection_operator():
    registered_user = RegisteredUser(username="testreguser", user_id=12346, flag=False)
    channel_name = "general_chat"
    registered_user += channel_name  # Assuming the overloaded operator adds the user to the channel
    assert channel_name in registered_user.channels

def test_user_flag_assignment():
    registered_user = RegisteredUser(username="testuser", user_id=12348, flag=False)
    assert registered_user.flag is False
    registered_user.flag = True
    assert registered_user.flag is True


""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bot Class Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def test_bot_initialization():
    bot = Bot(username="testbot", user_id=12349)
    assert bot.username == "testbot"
    assert isinstance(bot.__username, str)
    assert bot.user_id != None

def test_fun_fact_posting():
    bot = Bot(username="testbot", user_id=12349)
    fun_fact = bot.post_fun_fact()
    assert isinstance(fun_fact, str)
    assert "fun fact" in fun_fact.lower()

def test_bot_schedule_event():
    bot = Bot(username="testbot", user_id=12349)
    event = bot.schedule_event("meeting", datetime.now())
    assert isinstance(event, dict)
    assert event["name"] == "meeting"

def test_log_new_user():
    bot = Bot(username="testbot", user_id=12349)
    user_info = {"username": "newuser", "user_id": 12350}
    bot.log_new_user(user_info)
    assert "newuser" in bot.user_log

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Admin Class Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
@pytest.fixture
def test_admin_initialization():
    admin = Admin(username="admin", user_id=12351)
    assert admin.username == "admin"
    assert admin.user_id == 12351

def test_view_user_list():
    admin = Admin(username="admin", user_id=12351)
    user_list = admin.view_user_list()
    assert isinstance(user_list, list)
    assert len(user_list) > 0  # Assuming there are registered users

def test_update_channel_stats():
    admin = Admin(username="admins", user_id=12351)
    initial_stats = admin.channel_stats.copy()  # Make a copy of initial stats for comparison
    admin.update_channel_stats("general_chat", new_messages=10, new_users=2)
    assert admin.channel_stats[0] > initial_stats[0]  # Assuming the stat has increased

def test_message_log():
    admin = Admin(username="admin", user_id=12351)
    message = "test message"
    admin.log_message("testuser", message)
    assert "testuser" in admin.message_log
    assert admin.message_log["testuser"] == [message]
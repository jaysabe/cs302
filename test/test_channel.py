# # tests for Channel class and to test ui
# from ui.channel import Channel
# def test_channel_initialization():
#     channel = Channel("General", ["user1", "user2", "user3"])
    
#     assert channel.get_title() == "General"
#     assert channel.get_active_users() == ["user1", "user2", "user3"]
#     assert channel.get_key() == "general"
    
# def test_channel_build():
#     data = {
#         "title": "TechTalk",
#         "topics": ["AI", "Blockchain", "Cloud"]
#     }
#     channel = Channel.build(data)
    
#     assert isinstance(channel, Channel)
#     assert channel.get_title() == "TechTalk"
#     assert channel.get_active_users() == ["AI", "Blockchain", "Cloud"]
    
# def test_channel_str():
#     channel = Channel("General", ["user1", "user2", "user3"])
    
#     assert str(channel) == "<Channel: General>"
    
# def test_channel_contains():
#     channel = Channel("General", ["user1", "user2", "user3"])
    
#     assert "user1" in channel
#     assert "user4" not in channel
    
# def test_channel_add_remove_topic():
#     channel = Channel("General", ["user1", "user2", "user3"])
    
#     # Add a new topic
#     channel.add_topic("user4")
#     assert "user4" in channel.get_active_users()
    
#     # Remove an existing topic
#     channel.remove_topic("user2")
#     assert "user2" not in channel.get_active_users()
    
# def test_channel_lookup():
#     channel1 = Channel("General", ["user1", "user2"])
#     channel2 = Channel("TechTalk", ["user3", "user4"])
    
#     assert Channel.lookup("general") == channel1
#     assert Channel.lookup("techtalk") == channel2
#     assert Channel.lookup("nonexistent") is None
    
    
# def test_channel_to_dict():
#     channel = Channel("General", ["user1", "user2", "user3"])
#     expected_dict = {
#         "_id": "general",
#         "title": "General",
#         "users": ["user1", "user2", "user3"]
#     }
    
#     assert channel.to_dict() == expected_dict
    
# def test_channel_delete():
#     channel = Channel("General", ["user1", "user2", "user3"])
    
#     # Ensure the channel exists in the map
#     assert "general" in Channel._Channel__map
    
#     # Delete the channel and check if it is removed
#     channel.delete()
#     assert "general" not in Channel._Channel__map
    

# # Placeholder test for when BST implementation starts TODO:
# def test_channel_add_to_database():
#     # channel = Channel("General", ["user1", "user2", "user3"])
    
#     # # This should not raise any exceptions
#     # channel.add_to_database()
#     pass


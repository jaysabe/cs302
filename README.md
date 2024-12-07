# User Management System (UMS)

## Project Overview

This program consists of two main components developed across Project 4 and Project 5, forming a complete User Management System (UMS). The system is built around a class hierarchy for user roles (Project 4) and utilizes a Binary Search Tree (BST) for efficient data storage and retrieval of user information (Project 5).

## Key Features

A class hierarchy to represent different user roles: User, RegisteredUser, Bot, and Admin.
A Binary Search Tree (BST) implementation for managing users in an organized and efficient manner.
Dynamic memory management and use of polymorphism to allow flexible interaction with users of different roles.

## Project 4: User Role Hierarchy

### Description

Project 4 establishes the core hierarchy for the User Management System. It defines the user roles and their distinct permissions and behaviors.

### Classes and Design

1. User (Base Class)
   The abstract base class for all user types.
   Contains core attributes like username and userID.
   Provides virtual methods for subclasses to override.
2. RegisteredUser (Derived Class)
   Represents a standard registered user.
   Includes functionality for joining channels and interacting with other users.
3. Bot (Derived Class)
   A specialized user for automating tasks.
   Features include:
   Post Fun Facts: Automatically posts fun facts in a channel.
   Event Scheduling: Handles reminders and events.
   User Activity Logging: Tracks user activities.
4. Admin (Derived Class)
   Represents a user with elevated permissions.
   Abilities include:
   Moderating channels.
   Managing registered users and bots.
   Viewing and editing system logs.
   Project 5: Binary Search Tree for User Management
   Description
   Project 5 builds on the hierarchy from Project 4 by integrating a Binary Search Tree (BST) to store and manage users. The tree enables fast and organized storage, retrieval, and manipulation of user data.

### Key Features

- Inorder Traversal: Used for sorted display of user information.
- Insertion and Deletion: Add and remove users dynamically.
- Search: Quickly locate users by username or userID.
  Custom Objects: Each tree node stores a User object or its derived types (RegisteredUser, Bot, Admin).

#### Tree Structure

Nodes: Each node in the tree contains: - A reference to a User object.
References to the left and right child nodes.
Root: The tree's root node serves as the entry point for all operations.
Implementation Details
Uses dynamic memory management to create, link, and delete nodes.
Employs polymorphism for upcasting and downcasting of User objects during traversal.
Ensures memory safety using smart pointers (e.g., std::unique_ptr) for certain tree operations.

## Usage Instructions

### Setup

1. Clone the repository.
2. Navigate to the project4 or project5 directory.
3. Running the Program
4. Run the program using the following commands:

```bash
python -m src.ui.consule_ui
```

## Features Demonstration

- Add Users: Insert new users into the system.

### Role-Specific Features

- Registered users can join channels.
- Bots automate tasks like posting fun facts.

### Admins manage users and channels

- Display Users: Traverse the BST to view sorted user data.
- Search Users: Retrieve user information by username or userID.

## File Structure

```graphql
project4/
│
├── src/
│ ├── ui/
│ │ ├── main.py # Entry point for the program.
│ ├── logic/
│ │ ├── user.py # Core User hierarchy.
│ │ ├── bot.py # Bot implementation.
│ │ ├── admin.py # Admin implementation.
│ │ ├── tree.py # Node and BST classes.
│
└── tests/ # Unit tests for Project 4.
```

### Future Work

- Add persistence to store user data in external files or databases.
- Implement advanced search and filtering options.
- Extend functionality to include real-time multi-user interactions.

  Author Jay Abegglen
  Class: CS 302
  Projects: #4 and #5#

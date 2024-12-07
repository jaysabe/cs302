from logic.r_user import RegisteredUser
# *****************************************************************************
# Author:      Jay Abegglen
# Date:        11/31/2024
# Class:       CS 302
# Project:     Programming Assignment #4/5
# File Name:   main.py
# Purpose:     This file contains the interfaces for the Node and Tree classes.
# *****************************************************************************
class Node:
    def __init__(self, user_obj: RegisteredUser) -> None:
        self.__user_obj = user_obj
        self.__left = None
        self.__right = None

# **************************************************************************
# Function to overwrite the current data with new data.
#
# param: none
#
# return: none
# **************************************************************************         
    def update_data(self, user_obj: RegisteredUser) -> None:
        self.__user_obj = user_obj
        return  
# **************************************************************************
# Function to check if the node's left child reference is not None.
#
# param: none
#
# The function returns false if the node's left child reference is None. 
# Otherwise, the function returns true if the node's left child reference
# is not None.
# **************************************************************************
    def has_left(self) -> bool:
        return self.__left != None


# **************************************************************************
# Function to check if the node's right child reference is not None.
#
# param: none
#
# The function returns false if the node's right child reference is None. 
# Otherwise, the function returns true if the node's right child reference
# is not None.
# **************************************************************************
    def has_right(self) -> bool:
        return self.__right != None

# **************************************************************************
# Function to set the node's left child reference to a new value.
#
# new_left is passed the value of the new left child reference.
#
# return: none
# **************************************************************************
    def set_left(self, new_left: 'Node') -> None:
        self.__left = new_left
        return 


# **************************************************************************
# Function to set the node's right child reference to a new value.
#
    # new_right is passed the value of the new right child reference.
    #
    # return: none
    # **************************************************************************
    def set_right(self, new_right: 'Node') -> None:
        self.__right = new_right
        return 

# **************************************************************************
# Function to return the node's left child reference.
#
# param: none
#
# The function returns the node's left child reference.
# **************************************************************************
    def get_left(self) -> 'Node':
        return self.__left

# **************************************************************************
# Function to return the node's right child reference.
#
# param: none
#
# The function returns the node's right child reference.
# **************************************************************************
    def get_right(self) -> 'Node':
        return self.__right

# **************************************************************************
# Function to return the node's data
#
# param: none
#
# The function returns the node's data.
# ************************************************************************** 
    def get_data(self) -> int:
        return self.__user_obj   

#Interface for the Tree class that will represent a binary search tree   
class Tree: 
    def __init__(self) -> None:
        self.__root = None 
# **************************************************************************
# Wrapper function to insert a new data item into a BST.
#
# data is passed as the username and user_id into tree.
#
# return: none
# ************************************************************************** 
    def insert(self, data: int) -> None:
        self.__root = self.__insert_recursive(self.__root, data)
        return       
# **************************************************************************
# Recursive function to insert a new data item into a BST.
#
# root is passed an object reference to the node being traversed.
#
# data is passing the username and user_id to the tree
#
# The function returns the newly created node.
# **************************************************************************     
    def __insert_recursive(self, root:Node, data: RegisteredUser) -> Node:
    # Inserts the user item as a leaf
        if root == None:
            root = Node(data)
            return root
        if data.userid < root.get_data():
            root.set_left(self.__insert_recursive(root.get_left(), data))
        
        else:
            root.set_right(self.__insert_recursive(root.get_right()))
    
        return root
# **************************************************************************
# Wrapper function to display the data in the BST in sorted order.
#
# param: none
#
# The function returns the number of registered users displayed.
# ************************************************************************** 
    def display(self) -> int:

        #Returns 0 to the calling routine if the BST is empty.
        if self.__root == None:
            return 0

        return self.__display_recursive(self.__root)
    
     # **************************************************************************
    # Recursive function to display the data in the BST in sorted order.
    #
    # root is passed an object reference to the node being traversed.
    #
    # The function returns the number of data items displayed.
    # ************************************************************************** 
    def __display_recursive(self, root: Node) -> int:
        #Stops the recursive downward traversal down the current path of the 
        #tree and returns 0 to the calling routine if root is None.
        if root == None:
            return 0

        count = 0

        #Traverses the left subtree.
        count += self.__display_recursive(root.get_left())

        #Displays the data in the current node.
        print(root.get_data(), end =' ')

        #Traverses the left subtree.
        count += self.__display_recursive(root.get_right())

        return count + 1

# **************************************************************************
    # Wrapper function to retrieve a data item from the BST.
    #
    # key is passed the value corresponding to the data item to be retrieved
    #
    # The function returns -1 if the BST is empty, 0 if the data item cannot
    # be found, or 1 if the data item was found.
    # ************************************************************************** 
    def retrieve(self, key: int) -> int:
        #Returns -1 to the calling routine if the BST is empty.
        if self.__root == None:
            return -1

        return self.__retrieve_recursive(self.__root, key)
    
     # **************************************************************************
    # Recursive function to remove a data item from the BST.
    #
    # key is passed the value corresponding to the registered user to be removed.
    #
    # The function returns 0 if the data item cannot be found. Otherwise, the 
    # function returns the data item if it was found.
    # ************************************************************************** 
    def __retrieve_recursive(self, root: Node, key: int) -> RegisteredUser:
        if root == None:
            return 0 

        # if the curr node's data matches the key...
        if root.get_data() == key:
            return root.get_data()
        
        # Traverses the left subtree if the key is less than the current node's data
        if key < root.get_data():
            result, new_node = self.__remove_recursive(root.get_left(), key)
            root.set_left(new_node)
            
            # Traverses the right subtree if the key is greater than or equal to the current node's data
        else:
            result, new_node = self.__remove_recursive(root.get_right(), key)
            
        return result, root
    
    

    # **************************************************************************
    # Recursive function to remove a data item from the BST.
    #
    # key is passed the value corresponding to the data item to be removed.
    #
    # The function returns 0 if the data item cannot be found, or 1 if the data 
    # item was found and removed.
    # ************************************************************************** 
    def __remove_recursive(self, root: Node, key: int) -> int:
        #Stops the recursive downward traversal down the current path of the 
        #tree and returns 0 to the calling routine if root is None.
        if root == None:
            return 0, root
        
        io_successor = 0    
        temp_node = None    
        new_node = None

        #If the current node's data matches the key...
        if root.get_data() == key:

            #If the current node has a left child but not a right child...
            if root.has_left() and not root.has_right:

                #Saves the current node's left child reference.
                new_node = root.get_left()

            #If the current node has a left child but not a right child...
            elif not root.has_left() and root.has_right():

                #Saves the current node's right child reference.
                new_node = root.get_right()

            #If the current node has a left child and a right child...
            elif root.has_left() and root.has_right():


                #If the current node's right child does not have a left child...
                if not root.get_right().has_left():

                    #Replace the current node's data with its right child's
                    #data and assign the current node's right child reference
                    #to reference its right child's right child.
                    root.update_data(root.get_right().get_data())
                    root.set_right(root.get_right().get_right())

                #Otherwise...
                else:
                    io_successor, temp_node = self.__find_io_successor(root.get_right())
                    root.update_data(io_successor)

                new_node = root

            return 1, new_node
             
        result = 0
 
        #Traverses the left subtree if the key is less than the current node's
        #data.
        if key < root.get_data():
            result, new_node = self.__remove_recursive(root.get_left(), key)
            root.set_left(new_node)

        #Traverses the right subtree if the key is greater than or equal to 
        #the current node's data.
        else:
            result, new_node = self.__remove_recursive(root.get_right(), key)
            root.set_right(new_node)
                
        return result, root


    # **************************************************************************
    # Recursive function to remove and return the inorder successor's data item.
    #
    # root is passed an object reference to the node being traversed.
    #
    # The function returns 0 if the data item cannot be found, or 1 if the data 
    # item was found and removed.
    # ************************************************************************** 
    def __find_io_successor(self, root: Node):

        #If the current node does not have a left child...
        if not root.has_left():

            #Saves the current node's data and the reference to its right child.
            root_data = root.get_data()
            right_child = root.get_right()

            #Return the current node's data and a reference to its right
            #child.
            return root_data, right_child

        #Traverses the left subtree.
        io_successor, new_left = self.__find_io_successor(root.get_left())

        #Sets the current node's left child reference to new_left.
        root.set_left(new_left)

        return io_successor, root


if __name__ == '__main__':
    pass
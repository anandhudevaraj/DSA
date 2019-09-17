"""
Learning linked_list implementation in Python
"""


class Node:
    """
    Node class to represent linked list node
    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    """
    Class to initialise a linked list object
    """

    def __init__(self, value):
        self.first_node = Node(value)

    def add_node(self, value, position=None):
        if not self.first_node:
            self.first_node = Node(value)
        last_node = self.first_node
        if position == 0:
            self.first_node = Node(value, self.first_node)
            return
        elif position == None:
            while last_node.next_node:
                last_node = last_node.next_node
        elif position > 0:
            while (position - 1 > 0):
                last_node = last_node.next_node
                position -= 1
        last_node.next_node = Node(value, last_node.next_node)

    def print_nodes(self):
        node = self.first_node
        if not node:
            print("Empty List")
            return
        print node.value
        while node.next_node:
            node = node.next_node
            print node.value

    def delete_node(self, position=None, value=None):
        node = self.first_node
        current_position = 0
        if value:
            while True:
                if not node.value == value:
                    current_position += 1
                else: break
            else:
                print "{} not found in linked list".format(value)
                return

        if position == 0:
            self.first_node = self.first_node.next_node \
                if self.first_node.next_node else None
        else:
            if value: position = current_position
            while position - 1 > 0:
                node = node.next_node
            node.next_node = node.next_node.next_node

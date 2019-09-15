"""
Learning linked_list implementation in Python
"""


class LinkedList():
    """
    Class for initialising linked list object.
    """

    def __init__(self):
        self.list_obj = []

    def add_last(self, value):
        self.list_obj.append(value)

    def print_list(self):
        print("Current list is :: {}".format(self.list_obj))


list_1 = LinkedList()
list_1.add_last(4)
list_1.add_last(5)
list_1.print_list()

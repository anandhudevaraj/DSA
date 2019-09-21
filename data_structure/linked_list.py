"""
Learning linked_list implementation in Python
"""


# #
# #
# # class LinkedList():
# #     """
# #     Class for initialising linked list object.
# #     """
# #
# #     def __init__(self):
# #         self.list_obj = []
# #
# #     def add_last(self, value):
# #         self.list_obj.append(value)
# #
# #     def print_list(self):
# #         print("Current list is :: {}".format(self.list_obj))
# #
# #
# # list_1 = LinkedList()
# # list_1.add_last(4)
# # list_1.add_last(5)
# # list_1.print_list()
#
#
# class Node(object):
#     def __init__(self, value, next_node = None):
#         self.value = value
#         self.next_node = next_node
#
#     def add_item(self, next_node):
#         self.next_node = next_node
#
#
# def add_node(node_obj, position = 0, value = None):
#     ex_node = node_obj
#     if not position:
#         ex_node = Node(value, node_obj)
#         return ex_node
#     for pos in range(position-1):
#         ex_node = ex_node.next_node
#     ex_node.add_item(Node(value, ex_node.next_node))
#     return node_obj
#
#
# def print_nodes(node_obj):
#     print node_obj.value
#     while node_obj.next_node:
#         node_obj = node_obj.next_node
#         print node_obj.value
#
#
# x = Node(4)
# x.add_item(Node(5))
# x = add_node(x, 0, value=-1)
# x = add_node(x, 2, value='A')
#
# print_nodes(x)
class Node:
    """
    Node class to represent linked list node
    """

    def __init__(self):
        print("Hello World")

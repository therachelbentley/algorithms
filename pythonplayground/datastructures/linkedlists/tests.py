from datastructures.linkedlists import Node
from datastructures.linkedlists.singly_linked_list import SinglyLinkedList


# TODO: write better tests
list = SinglyLinkedList()
list.insert_one("!")
list.insert_one("world")
list.insert_one("hello")
assert list.size() == 3
assert list.delete_one("!")
assert list.size() == 2
assert list.delete_one("DNE") == None
assert list.size() == 2
assert list.find_one("hello")
assert list.delete_one("hello")
assert list.size() == 1
assert list.delete_one("world")
assert list.size() == 0

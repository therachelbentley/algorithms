from datastructures.linkedlists import Node
from datastructures.linkedlists.singly_linked_list import SinglyLinkedList
from datastructures.linkedlists.doubly_linked_list import DoublyLinkedList


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
assert list.update_one("world", "globe")
assert list.size() == 1
assert list.delete_one("world") == None
assert list.size() == 1
assert list.delete_one("globe")
assert list.size() == 0


d_list = DoublyLinkedList()
assert d_list.size() == 0
d_list.insert_one("world")
d_list.insert_one("hello")
assert d_list.size() == 2
assert d_list.update_one("world", "globe")
assert d_list.size() == 2
assert d_list.delete_one("hello")
assert d_list.size() == 1
assert d_list.find_one("hello") == None

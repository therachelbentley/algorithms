from datastructures.linkedlists import LinkedList
from datastructures.linkedlists import Node


class DoublyLinkedList(LinkedList):

    def __init__(self, head=None):
        super(DoublyLinkedList, self).__init__(head)

    def insert_one(self, data):
        """ Inserts a node into the head of the list.

            Runtime:
                O(1)
        """

        # create a new node
        new_node = Node(data)

        # if there is a node at head
        # then set previous to be new node
        if self.head:
            self.head.set_prev(new_node)

        # set new node to point next
        # to current head
        new_node.set_next(self.head)

        # set new node to have no
        # prev node
        new_node.set_prev(None) 

        # head should now be at new node
        self.head = new_node
   
    def delete_one(self, data):
        """ Removes the first occurence
            of data found in the list.

            Runtime:
                O(N) for worst case where
                N is the size of the list.

            Returns:
                The deleted node if found.
                None if no node was deleted.
        """

        # start at head
        current = self.head

        # since prev and next info is on node
        # just use the find one method
        node = self.find_one(data)

        # if a node is found then 
        # leap over that node in the list
        if node:
            previous_node = node.get_prev()
            next_node = node.get_next()

            if previous_node:
                previous_node.set_next(next_node)
            else:
                self.head = next_node

            if next_node:
                next_node.set_prev(previous_node)
            
            return node
            

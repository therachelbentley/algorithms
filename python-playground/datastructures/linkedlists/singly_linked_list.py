from datastructures.linkedlists import LinkedList
from datastructures.linkedlists import Node


class SinglyLinkedList(LinkedList):
    """ Class for a Singly Linked List.
    """

    def __init__(self, head=None):
        super(SinglyLinkedList, self).__init__(head)

    def insert_one(self, data):
        """ Inserts data into the list.
        
            Runtime:
                O(1)
        """
        new_node = Node(data)

        # set new node to point to the head
        new_node.set_next(self.head)

        # now set head to the new node
        self.head = new_node

    def delete_one(self, data):
        """ Deletes the first occurence of data.
        
            Runtime:
                O(N) for worst case,
                where N is the size of
                the linked list.

            Returns:
                The node if data is found.
                None if data is not found.
        """
        # start at head of list
        current = self.head

        # since starting at head, there is no previous node
        previous_node = None

        while current:

            # if the data matches, 
            # then need to make previous node
            # leap over current node
            if current.get_data() == data:

                # get the next node in the list
                next_node = current.get_next()

                # if a previous node does exist
                # then set that node's pointer 
                # to next_node
                if previous_node:
                    previous_node.set_next(next_node)
                # else set the head to next_node
                else:
                    self.head = next_node

                # since we found a match
                # and made previous node 
                # move its pointer
                # can leave the loop
                return current
            else:
                previous_node = current
                current = current.get_next()

from abc import ABCMeta


class LinkedList:
    __metaclass__ = ABCMeta

    def __init__(self, head):
        self.head = head

    def size(self):
        """ Gets the size of the list.

            Runtime:
                O(N) where N is the size of the list.

            Returns:
                The the size of the list.

        """

        # start at head of list
        current = self.head
        count = 0

        # keep count while traversing through list
        while current:
            count += 1
            current = current.get_next()

        return count 

    def find_one(self, data):
        """ Finds the first occurence of data.

            Runtime:
                O(N) for worst case where N
                is the size of the list.

            Returns:
                Node if data is found.
                None if data is not found.
        """
        
        # start at head of list
        current = self.head

        # traverse through list until data is found
        while current:

            # once data is found return that node
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()

    def update_one(self, data, new_data):
        """ Update a node's data.

            Runtime:
                O(N) for worst case where
                N is the size of the list.

            Returns:
                The updated node if found.
                None if no node was updated.
        """
        
        # find the node
        node = self.find_one(data)

        # if node is found, update data, and return node
        if node:
            node.set_data(new_data)
            return node

    def insert_one(self, data):
        raise NotImplementedError()
    
    def remove_one(self, data):
        raise NotImplementedError()

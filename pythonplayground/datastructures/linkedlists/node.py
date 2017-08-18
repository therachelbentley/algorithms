

class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    
    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node



class Node(object):

    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_prev(self, prev_node):
        self.prev_node = prev_node

    def get_prev(self):
        return self.prev_node
    
    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node

from algorithms.data_structures import util

class Traverse():

    def __init__(self, tree):
        self._tree = tree
        self._tree_size = len(tree)

    def in_order(self):
        order_of_traversal = []
    
        def traverse(node):
            if node >= self._tree_size:
                return
            traverse(util.get_left_child(node))
            order_of_traversal.append(self._tree[node])
            traverse(util.get_right_child(node))
        traverse(0)
        
        return order_of_traversal

    def pre_order(self):
        order_of_traversal = []
    
        def traverse(node):
            if node >= self._tree_size:
                return
            order_of_traversal.append(self._tree[node])
            traverse(util.get_left_child(node))
            traverse(util.get_right_child(node))
        traverse(0)
        
        return order_of_traversal

    def post_order(self):
        order_of_traversal = []
    
        def traverse(node):
            if node >= self._tree_size:
                return
            traverse(util.get_left_child(node))
            traverse(util.get_right_child(node))
            order_of_traversal.append(self._tree[node])
        traverse(0)
        
        return order_of_traversal

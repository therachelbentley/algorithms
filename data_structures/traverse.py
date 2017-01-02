from algorithms.data_structures import util

class Traverse(object):

    def __init__(self, tree):
        self._tree = tree
        self._tree_size = len(tree)


    # order of exploration: left, root, right
    # starts at bottom-left node and explores
    # its parent and their right child
    # example
    #   tree: [1, 2, 3, 4, 5]
    #   traversal: [4, 2, 5, 1, 3]
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


    # order of exploration: root, left, right
    # starts at root node and traverses down
    # the left side of the tree until it reaches
    # the bottom-left node. from their it will
    # look at bottom-left node's sibling (aka its
    # parent's right child)
    # example
    #   tree: [1, 2, 3, 4, 5]
    #   traversal: [1, 2, 4, 5, 3]
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


    # order of exploration: left, right, root
    # starts at bottom-left node and traverses
    # the leaves from left-most node to the
    # right-most node
    # example
    #   tree: [1, 2, 3, 4, 5]
    #   traversal: [4, 5, 2, 3, 1]
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

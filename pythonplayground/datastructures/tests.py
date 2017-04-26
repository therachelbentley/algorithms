from datastructures.traverse import Traverse


traverse = Traverse([4, 2, 5, 1, 3])
assert traverse.in_order() == [1, 2, 3, 4, 5]
assert traverse.pre_order() == [4, 2, 1, 3, 5]
assert traverse.post_order() == [1, 3, 2, 5, 4]

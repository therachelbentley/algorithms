

def _get_left_child(i):
    return (2 * i) + 1

def _get_right_child(i):
    return (2 * i) + 2

def _get_parent(i):
    return (-(-i // 2)) - 1

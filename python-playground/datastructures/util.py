

def get_left_child(i):
    return (2 * i) + 1

def get_right_child(i):
    return (2 * i) + 2

def get_parent(i):
    return (-(-i // 2)) - 1

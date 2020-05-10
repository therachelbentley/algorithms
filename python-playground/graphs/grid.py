

HORIZONTAL_RISK = .9
VERTICAL_RISK = .5


def get_risk(position):
    row = position[0]
    column = position[1]

    horizontal_risk = HORIZONTAL_RISK / 2**row
    vertical_risk = VERTICAL_RISK / 2**column

    return (horizontal_risk, vertical_risk)


grid = [
    ["a", "b", "c", "d"],
    ["e", "f", "g", "h"],
    ["i", "j", "k", "l"],
    ["m", "n", "o", "p"]
]



visited = [
 [None, None, None, None],
 [None, None, None, None],
 [None, None, None, None],
 [None, None, None, None],
]


start = (0, 0)
end = (3, 3)


def get_left(position):
    row = position[0]
    column = position[1]

    new_column = column - 1
    if new_column > -1 and new_column < len(grid[0]):
        return (row, new_column)


def get_right(position):
    row = position[0]
    column = position[1]

    new_column = column + 1
    if new_column > -1 and new_column < len(grid[0]):
        return (row, new_column)


def get_up(position):
    row = position[0]
    column = position[1]

    new_row = row - 1
    if new_row > -1 and new_row < len(grid[0]):
        return (new_row, column)


def get_down(position):
    row = position[0]
    column = position[1]

    new_row = row + 1
    if new_row > -1 and new_row < len(grid[0]):
        return (new_row, column)


def dfs(position):
    if visited[position[0]][position[1]]:
        return
    visited[position[0]][position[1]] = True
    if position == end:
        print "FOUND"
        return

    up = get_up(position)
    if up:
        dfs(up)

    down = get_down(position)
    if down:
        dfs(down)

    left = get_left(position)
    if left:
        dfs(left)

    right = get_right(position)
    if right:
        dfs(right)

dfs(start)






visited = [
 [None, None, None, None],
 [None, None, None, None],
 [None, None, None, None],
 [None, None, None, None],
]


start = (0, 0)
end = (3, 3)


def get_children(position):
    children = []
    up = get_up(position)
    if up:
        children.append(up)
    down = get_down(position)
    if down:
        children.append(down)
    left = get_left(position)
    if left:
        children.append(left)
    right = get_right(position)
    if right:
        children.append(right)
    return children


queue = [start]

while queue:
    position = queue.pop(0)
    print position
    if visited[position[0]][position[1]]:
        continue
    visited[position[0]][position[1]] = True
    if position == end:
        print "FOUND BFS END"
        break
    children = get_children(position)

    if children:
        queue.extend(children)


print visited

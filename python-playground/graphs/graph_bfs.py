

class Solution(object):

    def __init__(self):
        #self.grid = ["@.a.#","###.#","b.A.B"]
        self.grid = ["@..aA","..B#.","....b"]
        self.visited = []
        for i in xrange(len(self.grid)):
            inside = []
            for j in xrange(len(self.grid[0])):
                inside.append(False)
            self.visited.append(inside)

    def look_up(self, i, j):
        x = i-1
        if x < 0:
            return None
        if self.visited[x][j]:
            return None
        return (x, j)

    def look_down(self, i, j):
        x = i+1
        if x >= len(self.grid):
            return None
        if self.visited[x][j]:
            return None
        return (x, j)

    def look_left(self, i, j):
        y = j-1
        if y < 0:
            return None
        if self.visited[i][y]:
            return None
        return (i, y)

    def look_right(self, i, j):
        y = j+1
        if y >= len(self.grid[0]):
            return None
        if self.visited[i][y]:
            return None
        return (i, y)

    def bfs(self):
    	queue = [(0, 0)]
    	keys = set()
        known_keys = set()
    	path = []
        optimized_path = []

    	while queue:
    	    i, j = queue.pop(0)
            self.visited[i][j] = True

    	    cell = self.grid[i][j]
            print cell
            print i, j
            print "\n"
            path.append((cell, (i, j)))

            if cell.isalpha():
                if cell.islower():
                    keys.add(cell)
                    known_keys.add(cell)
                    # i want to record the path leading up to the first key
                    # do you back track? I have the current position,
                    # do i go back through the path

                    optimized_path.append(cell)
                    current_cell = cell
                    # this gives me clues on how many keys there are
@ b B .
                    queue = []
                    path = []
                elif cell.lower() not in keys:
                    known_keys.add(cell)
                    # may need to add unvisit b/c
                    # I could treat the door like a wall if
                    continue
            elif cell == "#":
                continue


            # should we mark it as visited as it goes into the queue?
            # this would avoid going to the same location twice
            up = self.look_up(i, j)
    	    if up:
                queue.append(up)
                self.visited[up[0]][up[1]] = True

            down = self.look_down(i, j)
    	    if down:
                queue.append(down)
                self.visited[down[0]][down[1]] = True

            left = self.look_left(i, j)
    	    if left:
                queue.append(left)
                self.visited[left[0]][left[1]] = True

            right = self.look_right(i, j)
    	    if right:
                queue.append(right)
                self.visited[right[0]][right[1]] = True

            # i only want to place something in the queue if i can get to it
            # from a cell that i'm on

        print keys
        return path

        # maybe i find the shortest path to the first key
        # then find the shortest path to the next key
        # so as I'm going through BFS, the first time I hit a key
        # i add that path, reset the queue and start from that key



solution = Solution()
print solution.bfs()
print solution.visited

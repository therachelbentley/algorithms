


class Reachability(object):


    def __init__(self, adjacency_list):
        self._a = adjacency_list
        self._vertices_visited = [0] * len(self._a)


    # checks if vertex y is reachable
    # from vertex x
    def reachable(self, x, y):
        # mark vertex as visited
        self._vertices_visited[x] = 1

        if y in self._a[x]:
            return True
        else:
            for vertex in self._a[x]:
                # if the vertex has not been visited
                # then go explore the adjacent vertices
                if self._vertices_visited[vertex] is 0:
                    explore = self.reachable(vertex, y)
                    if explore == True:
                        return explore

        return False

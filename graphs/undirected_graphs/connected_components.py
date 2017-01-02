


class ConnectedComponents(object):


    def __init__(self, adjacency_list):
        self._a = adjacency_list
        self._vertices_visited = [0] * len(self._a)
        self._graphs = {}


    def number_of_connected_components(self):
        # connected components number
        ccn = 1

        for vertex in range(0, len(self._a)):
            # if vertex has not been visited
            # then explore it
            if self._vertices_visited[vertex] is 0:
                self._graphs[ccn] = []
                self._explore(vertex, ccn)
                ccn += 1

        # return the number of graphs
        return len(self._graphs.keys())


    def _explore(self, vertex, ccn):
        self._vertices_visited[vertex] = 1
        self._graphs[ccn].append(vertex + 1)
        for w in self._a[vertex]:
            if self._vertices_visited[w] is 0:
                self._explore(w, ccn)

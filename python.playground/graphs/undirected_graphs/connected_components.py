

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


### TESTS ###
case_1 = [[1, 3], [0, 2], [1, 3], [2, 0]]
case_2 = [[1], [0, 2], [1], []]
case_3 = [[20, 89], [90], [], [], [82, 65], [8, 71, 30], [18, 90, 92, 35], [49], [5], [67, 88, 38], [88, 71, 60, 79], [21, 85], [71, 76, 66], [], [22, 16], [49], [82, 81, 14], [87], [6, 75, 66], [97, 53, 39, 90], [93, 0, 54, 49], [67, 57, 11, 68], [52, 55, 14], [75, 68], [60], [63, 56], [95], [41, 58, 73, 51], [], [31, 95, 52], [34, 5], [92, 29, 45], [], [93, 95], [30], [6], [37, 90], [85, 36, 43], [72, 9], [70, 19, 90], [], [97, 27, 94], [51], [74, 37, 93, 78, 53], [90], [31], [], [], [], [7, 15, 68, 65, 20], [], [42, 27], [22, 83, 29], [19, 43], [88, 72, 20], [22, 78], [25], [21], [27], [], [10, 24], [70], [91, 71], [25], [], [88, 49, 98, 4], [89, 67, 18, 12], [21, 66, 9], [49, 21, 73, 23], [], [74, 83, 39, 87, 61], [5, 62, 10, 12, 78], [54, 38], [27, 68], [70, 43], [99, 18, 23, 92], [12], [], [55, 71, 43], [10], [97], [16], [16, 4], [70, 52], [], [37, 11], [], [17, 70], [10, 54, 65, 9], [66, 0], [44, 36, 6, 1, 39, 19], [62, 94], [31, 75, 6], [20, 43, 33], [41, 91], [26, 29, 33], [], [80, 41, 19], [65], [75]]

c = ConnectedComponents(case_1)
assert c.number_of_connected_components() == 1

c = ConnectedComponents(case_2)
assert c.number_of_connected_components() == 2

c = ConnectedComponents(case_3)
assert c.number_of_connected_components() == 19

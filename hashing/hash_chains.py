

class HashChains(object):

    def __init__(self, cardinality):
        self._arr = [[] for i in range(cardinality)]

    def find(self, key, query):

        try:
            index = self._arr[key].index(query)
        except ValueError:
            index = -1

        return index

    def add(self, key, value):

        index = self.find(key, value)
        if index == -1:
            self._arr[key].append(value)

    def delete(self, key, value):

        index = self.find(key, value)
        if index != -1:
            self._arr[key].pop(index)



class DirectAddressing:

    def __init__(self, arr_size):
        self.arr = [None]*arr_size

    def find(self, n):
        return self.arr[n]

    def add(self, n, v):
        self.arr[n] = v

    def delete(self, n):
        self.arr[n] = None



class DirectAddressing(object):

    def __init__(self, arr_size):
        self.arr = [None]*arr_size

    def find(self, n):
        return self.arr[n]

    def add(self, n, v):
        self.arr[n] = v

    def delete(self, n):
        self.arr[n] = None


### TESTS ###
phone_book = DirectAddressing(10**7)
phone_book.add(5551234, "foo")
phone_book.add(5552345, "bar")
phone_book.delete(5551234)

assert phone_book.find(5551234) == None
assert phone_book.find(5552345) == "bar"

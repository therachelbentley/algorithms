

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


### TESTS ###
def _hash_ascii_character(string):
    if len(string) > 1:
        return ord(string[0])

foo_key = _hash_ascii_character("foo")
fizz_key = _hash_ascii_character("fizz")
bar_key = _hash_ascii_character("bar")

hash_chain = HashChains(256)
hash_chain.add(foo_key, 'foo')
hash_chain.add(bar_key, 'bar')
hash_chain.add(fizz_key, 'fizz')
hash_chain.delete(bar_key, 'bar')

assert hash_chain.find(bar_key, 'bar') == -1
assert hash_chain.find(foo_key, 'foo') == 0
assert len(hash_chain._arr[foo_key]) == 2

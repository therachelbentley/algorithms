from algorithms.hashing.direct_addressing import DirectAddressing
from algorithms.hashing.hash_chains import HashChains

### DirectAddressing Test ###
phone_book = DirectAddressing(10**7)
phone_book.add(5551234, "foo")
phone_book.add(5552345, "bar")
phone_book.delete(5551234)

assert phone_book.find(5551234) == None
assert phone_book.find(5552345) == "bar"


### HashChains Test ###
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

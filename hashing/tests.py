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
# TODO create hash function to test
hash_chain = HashChains(5)
hash_chain.add(4, 'foo')
hash_chain.add(4, 'bar')
hash_chain.add(2, 'foo')
hash_chain.delete(4, 'bar')
assert hash_chain.find(4, 'bar') == -1
assert hash_chain.find(2, 'foo') == 0

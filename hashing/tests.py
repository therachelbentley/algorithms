from algorithms.hashing.direct_addressing import DirectAddressing


phone_book = DirectAddressing(10**7)
phone_book.add(5551234, "foo")
phone_book.add(5552345, "bar")
phone_book.delete(5551234)
assert phone_book.find(5551234) == None
assert phone_book.find(5552345) == "bar"

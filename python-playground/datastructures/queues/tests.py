from datastructures.queues import ListQueue


list_queue = ListQueue()
list_queue.enqueue("hello")
list_queue.enqueue("World")
assert list_queue.size() == 2
assert list_queue.dequeue() == "hello"
assert list_queue.size() == 1

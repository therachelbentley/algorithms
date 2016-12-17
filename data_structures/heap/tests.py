from algorithms.data_structures.heap.min_heap import MinHeapSort


min_heap = MinHeapSort([5, 9, 38, 7, 5, 80])
assert min_heap.build_heap() == [5, 5, 38, 7, 9, 80]
min_heap = MinHeapSort([13, 11, 12, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6])
assert min_heap.build_heap() == [1, 2, 5, 7, 3, 6, 10, 13, 11, 8, 4, 9, 12]

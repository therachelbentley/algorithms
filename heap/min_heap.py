from algorithms.heap.util import _get_left_child, _get_right_child



class MinHeapSort():

    def __init__(self, arr):

        self._data = arr
        self._n = len(self._data)

    def _sift_down(self, i):
    
        min_index = i
        left_child = _get_left_child(i)
        right_child = _get_right_child(i)
        
        if left_child < self._n and self._data[left_child] < self._data[min_index]:
            min_index = left_child

        if right_child < self._n and self._data[right_child] < self._data[min_index]:
            min_index = right_child
      
        if i != min_index:
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self._sift_down(min_index)
  

    def _generate_min_heap(self):
    
        for i in range(self._n - 1, -1, -1):
            self._sift_down(i)

    def build_heap(self):

        self._generate_min_heap()
        return self._data


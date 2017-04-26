

class SelectionSort(object):

    def __init__(self, arr):
        self._arr = arr

    def sort_arr(self):

    	for i in range(len(self._arr)):

    		min_item = i

    		for j in range(i + 1, len(self._arr)):
    			if self._arr[min_item] > self._arr[j]:
    				min_item = j

    		self._arr[i], self._arr[min_item] = self._arr[min_item], self._arr[i]


    	return self._arr


### TESTS ###
s = SelectionSort([8, 5, 2, 6, 2,  2, 9, 3, 1, 4, 0, 7])
assert s.sort_arr() == [0, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]

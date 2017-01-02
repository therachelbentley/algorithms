import math


class MergeSort(object):

    def __init__(self, arr):
        self.arr = arr


    def sort_arr(self):
        return self._divide(self.arr)


    # divide the array into smaller arrays
    # until each array is of size 1
    # then call merge on each subarray
    def _divide(self, arr):
        arr_size = len(arr)

        if arr_size == 1:
            return arr

        i = int(math.ceil(arr_size/2.0))

        a = self._divide(arr[:i])
        b = self._divide(arr[i:])

        return self._merge(a, b)


    # takes two sorted arrays and
    # merges them together
    def _merge(self, a, b):

        sorted_arr = []

        a_size = len(a)
        b_size = len(b)

        a_index = 0
        b_index = 0

        while True:
            if a[a_index] < b[b_index]:
                sorted_arr.append(a[a_index])
                a_index += 1

                if a_index >= a_size:
                    sorted_arr = sorted_arr + b[b_index:]
                    break
            else:
                sorted_arr.append(b[b_index])
                b_index += 1

                if b_index >= b_size:
                    sorted_arr = sorted_arr + a[a_index:]
                    break

        return sorted_arr

from algorithms.sorting.selection_sort import SelectionSort


s = SelectionSort([8, 5, 2, 6, 2,  2, 9, 3, 1, 4, 0, 7])
assert s.sort_arr() == [0, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
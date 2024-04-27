import sys

import numpy as np
from Merge import merge_arrays


def sort(array, n_split):
    if len(array) % n_split != 0:
        print("It is not possible to split into so many subarrays because they will have different size")
        sys.exit(1)
    sub_arrays = np.array(array).reshape(n_split, -1)
    for sub_array in sub_arrays:
        selection_iterative_sort(sub_array)
    return merge_arrays(sub_arrays)


def selection_iterative_sort(array: list):
    size = len(array)
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

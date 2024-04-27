import multiprocessing as mp
import numpy as np
from Merge import merge_arrays


def selection_iterative_sort(array: list):
    size = len(array)
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def sort(array: list, n_split: int):
    if len(array) % n_split != 0:
        print("It is not possible to split into so many subarrays because they will have different size")
        return
    sub_arrays = np.array(array).reshape(n_split, -1)

    pool = mp.Pool(n_split)
    res = pool.map(selection_iterative_sort, sub_arrays)
    pool.close()
    pool.join()
    return merge_arrays(res)
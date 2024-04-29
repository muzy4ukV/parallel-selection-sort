import multiprocessing as mp
import sys
import numpy as np
from Merge import merge_arrays
from SelectionSort import selection_iterative_sort


def parallel_sort(array: list, n_split: int):
    """
    :param array: input array
    :param n_split: number of division of initial array
    :return:
    """
    if len(array) % n_split != 0:
        print("It is not possible to split into so many subarrays because they will have different size")
        sys.exit(1)
    sub_arrays = np.array(array).reshape(n_split, -1)

    pool = mp.Pool(n_split)
    res = pool.map(selection_iterative_sort, sub_arrays)
    pool.close()
    pool.join()
    return merge_arrays(res)

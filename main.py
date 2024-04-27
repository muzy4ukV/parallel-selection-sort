from random import randint

import ParallelSelectionSort
from Rifle import Rifle
from SelectionSort import SelectionSort
from copy import deepcopy
from time import time
from BidirectionalSelectionSort import parallel_sort


def test_sort_method(sort_method, len_array, progon_number):
    """
    This method tests sorting algo for correctness and measure its average time

    :param sort_method: Sorting method for testing
    :param len_array: Length of test array
    :param progon_number: Number of testing repeating
    :return average_time
    """
    array = [Rifle() for i in range(len_array)]
    # List for collecting time for each of progon
    exec_time = list()
    # Flag that will save the wrong sort error
    correctness_flag = True
    for i in range(progon_number):
        arr = deepcopy(array)

        # Start of measuring
        start = time()
        sort_method(arr)
        # End of measuring
        end = time()

        exec_time.append(end - start)
        if not check_array(arr):
            correctness_flag = False
        print(f"- {i + 1} progon passed -")
    print(f"Correctness of sorting: {correctness_flag}")
    avarage_time = sum(exec_time) / progon_number
    print("Average execution time:", avarage_time, "seconds")
    return avarage_time


def check_array(array):
    """
    Method checks if array are in ascending order

    :param array:
    :return:
    """
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True


def main():
    array = [randint(0, 10) for _ in range(10)]
    print(array)
    print(ParallelSelectionSort.sort(array, 5))






if __name__ == '__main__':
    main()

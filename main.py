from typing import Callable

from Rifle import Rifle
from copy import deepcopy
from time import time
import ParallelSelectionSort
import SelectionSort


def test_sort_method(sort_method: Callable, len_array: int, progon_number: int, n_split: int) -> float:
    """
    This method tests sorting algo for correctness and measure its average time

    :param sort_method: Sorting method for testing
    :param len_array: Length of test array
    :param progon_number: Number of testing repeating
    :param n_split: Number of array division
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
        arr = sort_method(arr, n_split)
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


def check_array(array: list[Rifle]) -> bool:
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
    serial_time = test_sort_method(SelectionSort.sort, 15000, 5, 5)

    parallel_time = test_sort_method(ParallelSelectionSort.parallel_sort, 15000, 5, 5)

    speedup = serial_time / parallel_time

    print("Speedup for parallel version is -", speedup)


if __name__ == '__main__':
    main()

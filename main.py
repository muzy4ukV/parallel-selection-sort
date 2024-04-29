from typing import Callable

import numpy as np

from Rifle import Rifle
from copy import deepcopy
from time import time
import ParallelSelectionSort
import SelectionSort
import matplotlib.pyplot as plt
import BidirectionalSelectionSort


def test_sort_method(sort_method: Callable, len_array: int, progon_number: int, n_split=None) -> float:
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
        if n_split:
            arr = sort_method(arr, n_split)
        else:
            arr = sort_method(arr)
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


def warm_up(len_array: int, progon_number: int):
    """
    Function that will warming up the processor before main work
    :return: None
    """
    print("Warming up CPU")
    array = [Rifle() for i in range(len_array)]
    for i in range(progon_number):
        SelectionSort.sort(array, 5)
        print(f"- {i + 1} progon passed -")
    print("Warming ended")


def print_plot():
    len_of_arrays = [1, 2, 5, 10, 20, 25, 50]
    progons = 5
    results_serial = list()
    for length in len_of_arrays:
        results_serial.append(test_sort_method(SelectionSort.sort, 10000, progons, length))
    results_paralel = list()
    for length in len_of_arrays:
        results_paralel.append(test_sort_method(ParallelSelectionSort.parallel_sort, 10000, progons, length))
    speedups = np.divide(results_serial, results_paralel)
    print("Results of algo testing")
    print("{:16s}   {:9s}   {:11s}   {:7s}".format("Number of splits", "Serial, s", "Parallel, s", "Speedup"))
    for i in range(len(len_of_arrays)):
        print("{:<15d}   {:9.2f}   {:11.2f}   {:7.3f}".format(len_of_arrays[i], results_serial[i], results_paralel[i], speedups[i]))

    plt.figure(figsize=(8, 5))
    plt.plot(len_of_arrays, results_serial, marker='o', linestyle='--', label="Serial, s", color='red')
    plt.plot(len_of_arrays, results_paralel, marker='o', linestyle='--', label="Parallel, s", color='green')
    plt.title('Час виконнання послідовного й паралельного алгоритмів')
    plt.xlabel('Кількість розбиттів масиву')
    plt.ylabel('Час виконання, с')
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(len_of_arrays, speedups, marker='o', linestyle='--')
    plt.title('Залежність прискорення від кількості розбиттів вхідного масиву')
    plt.xlabel('Кількість розбиттів масиву')
    plt.ylabel('Прискорення')
    plt.show()


def main():
    warm_up(10000, 5)

    # serial_time = test_sort_method(SelectionSort.sort, 15000, 5, 5)
    #
    # parallel_time = test_sort_method(ParallelSelectionSort.parallel_sort, 15000, 5, 5)
    #
    #
    # speedup = serial_time / parallel_time
    #
    # print("Speedup for parallel version is -", speedup)
    # print("Testing Parallel Selection Merge Sort")
    # test_sort_method(ParallelSelectionSort.parallel_sort, 1000, 10, 5)

    print_plot()


if __name__ == '__main__':
    main()

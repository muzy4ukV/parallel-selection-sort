import multiprocessing as mp


def find_min_max(arr, start, end):
    """
    Find the index of the minimum and maximum values in the array
    :param arr: input array
    :param start: start of subarray
    :param end: end of subarray
    :return: indexes of min and max
    """
    min_index = start
    max_index = start
    for i in range(start + 1, end):
        if arr[i] < arr[min_index]:
            min_index = i
        elif arr[i] > arr[max_index]:
            max_index = i
    return min_index, max_index


def parallel_sort(arr):
    size = len(arr)
    left = 0
    right = size
    middle = (left + right) // 2

    with mp.Pool(processes=2) as pool:
        while left < middle-1:

            t1 = pool.apply_async(find_min_max, (arr, left, middle))
            t2 = pool.apply_async(find_min_max, (arr, middle, right))

            left_min_idx, left_max_idx = t1.get()
            right_min_idx, right_max_idx = t2.get()

            if arr[left_min_idx] <= arr[right_min_idx]:
                min_idx = left_min_idx
            else:
                min_idx = right_min_idx
            arr[left], arr[min_idx] = arr[min_idx], arr[left]

            if arr[left_max_idx] <= arr[right_max_idx]:
                max_idx = right_max_idx
            else:
                max_idx = left_max_idx
            arr[right - 1], arr[max_idx] = arr[max_idx], arr[right - 1]

            left += 1
            right -= 1
    if arr[middle-1] > arr[middle]:
        arr[middle-1], arr[middle] = arr[middle], arr[middle-1]
    return arr
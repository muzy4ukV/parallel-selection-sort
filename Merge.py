def merge(arr1: list, arr2: list):
    """
    :param arr1, arr2: left and right subarray for merging
    :return: one merged sorted array
    """
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def merge_arrays(arrays):
    """
    :param arrays: input array of sorted sub_arrays
    :return: one merged sorted array
    """
    if len(arrays) == 0:
        return []
    if len(arrays) == 1:
        return arrays[0]
    if len(arrays) == 2:
        return merge(arrays[0], arrays[1])

    mid = len(arrays) // 2
    left_half = merge_arrays(arrays[:mid])
    right_half = merge_arrays(arrays[mid:])

    return merge(left_half, right_half)

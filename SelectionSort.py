class SelectionSort:
    """
    Class that contains a classic realisation of Selection Sort as a static method
    """
    @staticmethod
    def sort(array):
        size = len(array)
        for index in range(size - 1):
            min_index = index
            for i in range(index + 1, size):
                if array[i] < array[min_index]:
                    min_index = i
            array[index], array[min_index] = array[min_index], array[index]

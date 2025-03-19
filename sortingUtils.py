def isSorted(array):
    for x in range(len(array) - 1):
        if array[x] > array[x + 1]:
            return False
    return True
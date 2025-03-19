import sortingUtils
from sortingUtils import isSorted, wait

def bubbleSort(array, delay):
    while not isSorted(array) and sortingUtils.sorting:
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                wait(delay)
                sortingUtils.comparisons += 1
                if array[j] > array[j + 1]:
                    sortingUtils.swaps += 1
                    array[j], array[j + 1] = array[j + 1], array[j]
                    yield
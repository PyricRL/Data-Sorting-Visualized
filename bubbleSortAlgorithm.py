import sortingUtils
from sortingUtils import isSorted, wait, colorDataSet

def bubbleSort(array, delay):
    while not isSorted(array) and sortingUtils.sorting:
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                wait(delay)
                sortingUtils.comparisons += 1

                sortingUtils.selectedIndices.clear()
                sortingUtils.comparedIndices.clear()

                sortingUtils.selectedIndices.append(j + 1)
                if array[j] > array[j + 1]:
                    sortingUtils.swaps += 1
                    sortingUtils.comparedIndices.append(j)
                    array[j], array[j + 1] = array[j + 1], array[j]
                    yield
    
    colorDataSet(array, len(array))
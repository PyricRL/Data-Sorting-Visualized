import time

import sortingUtils
from sortingUtils import isSorted, wait

def countSort(array, delay):
    while not isSorted(array):
        startTime = time.perf_counter()
        M = max(array)

        count_array = [0] * (M + 1)

        sortingUtils.selectedIndices.clear()

        for num in array:
            count_array[num] += 1

        for i in range(1, M + 1):
            count_array[i] += count_array[i - 1]

        output_array = [0] * len(array)

        for i in range(len(array) - 1, -1, -1):
            output_array[count_array[array[i]] - 1] = array[i]
            count_array[array[i]] -= 1
            sortingUtils.swaps += 1
            sortingUtils.swapDataSound.play()
            sortingUtils.selectedIndices.append(i)
            yield
            wait(delay)
        
        sortingUtils.sortTimeVisual = time.perf_counter() - startTime

def countSortNoVisible(array):
    while not isSorted(array):
        startTime = time.perf_counter()
        M = max(array)

        count_array = [0] * (M + 1)

        for num in array:
            count_array[num] += 1

        for i in range(1, M + 1):
            count_array[i] += count_array[i - 1]

        output_array = [0] * len(array)

        for i in range(len(array) - 1, -1, -1):
            output_array[count_array[array[i]] - 1] = array[i]
            count_array[array[i]] -= 1
            sortingUtils.swaps += 1
            sortingUtils.swapDataSound.play()
            sortingUtils.selectedIndices.append(i)
        
    sortingUtils.sortTime = time.perf_counter() - startTime
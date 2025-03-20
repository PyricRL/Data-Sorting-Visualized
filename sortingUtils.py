import time
import pygame

def isSorted(array):
    for x in range(len(array) - 1):
        if array[x] > array[x + 1]:
            return False
    return True

def wait(delayMS):
    if delayMS <= 0:
        return None
    end_time = time.perf_counter() + (delayMS / 1000.0)
    while time.perf_counter() < end_time:
        pass

def colorDataSet(array, length):
    selectedIndices.clear()
    comparedIndices.clear()

    print(length)

    for i in range(length):
        selectedIndices.append(array[i] - 1)
        wait(50)
        yield
    yield

sorting = False

swaps = 0
comparisons = 0

colorAnim = None

selectedIndices = []
comparedIndices = []
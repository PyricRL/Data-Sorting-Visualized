import time

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

sorting = False

swaps = 0
comparisons = 0
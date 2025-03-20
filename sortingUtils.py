import time
import pygame
import random

pygame.init()

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

    for i in range(length):
        selectedIndices.append(array[i] - 1)
        finishDataSound.play()
        yield
    yield

def createTestData(length):
    for x in range(length):
        data.append(x + 1)
    
    random.shuffle(data)

sorting = False

data = []

swaps = 0
comparisons = 0

colorAnim = None

selectedIndices = []
comparedIndices = []

sortTime = 0
sortTimeVisual = 0

swapDataSound = pygame.mixer.Sound('audio/dataSort.wav')
swapDataSound.set_volume(0.1)

finishDataSound = pygame.mixer.Sound('audio/dataFinish.wav')
finishDataSound.set_volume(0.1)

algorithmName = ""

currentSort = 1

delay = 100
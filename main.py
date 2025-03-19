import pygame
import random

from sortingUtils import *
from bubbleSortAlgorithm import bubbleSort
from bogoSortAlgorithm import bogoSort

WIDTH, HEIGHT = 1280, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

sorting = True

data = []

def createTestData(length):
    for x in range(length):
        data.append(x + 1)
    
    random.shuffle(data)

createTestData(100)

def showDataToScreen(array):
    SCREEN.fill("black")
    gap = WIDTH // len(array)
    for x in range(len(array)):
        rect = (x * gap, HEIGHT - array[x], gap - 1, array[x])
        pygame.draw.rect(SCREEN, "white", rect)

def main():
    global sorting
    running = True
    sorting = False

    sortingAlgorithms = {
    "Bubble Sort": bubbleSort,
    "Bogo Sort": bogoSort,
    }

    selectedSort = "Bubble Sort"
    generator = sortingAlgorithms[selectedSort]
    generatorFunc = generator(data, 500)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sorting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sorting = True
                    try:
                        next(generatorFunc)
                    except StopIteration:
                        sorting = False
        SCREEN.fill("black")

        showDataToScreen(data)
        pygame.display.flip()

if __name__ == "__main__":
    main()
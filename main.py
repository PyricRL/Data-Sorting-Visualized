import pygame
import random

pygame.init()

import sortingUtils
from sortingUtils import colorDataSet
from bubbleSortAlgorithm import bubbleSort
from bogoSortAlgorithm import bogoSort

WIDTH, HEIGHT = 1280, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

data = []

def createTestData(length):
    for x in range(length):
        data.append(x + 1)
    
    random.shuffle(data)

createTestData(10)

def showDataToScreen(array):
    scaleFactor = (HEIGHT - 50) / max(array)
    SCREEN.fill("black")
    gap = WIDTH // len(array)
    for x in range(len(array)):
        if x in sortingUtils.comparedIndices:
            color = "red"
        elif x in sortingUtils.selectedIndices:
            color = "green"
        else:
            color = "white"
        rect = (x * gap, HEIGHT - (array[x] * scaleFactor), gap - 1, array[x] * scaleFactor)
        pygame.draw.rect(SCREEN, color, rect)

def displayStats():
    font = pygame.font.SysFont('Times New Roman', 20)
    stats_text = font.render(f"Swaps: {sortingUtils.swaps} | Comparisons: {sortingUtils.comparisons}", True, (255, 255, 255))
    SCREEN.fill("black", (10, 10, 1000, 30))
    SCREEN.blit(stats_text, (10, 10))

def main():
    running = True

    sortingAlgorithms = {
    "Bubblesort": bubbleSort,
    "Bogosort": bogoSort,
    }

    selectedSort = "Bogosort"
    generator = sortingAlgorithms[selectedSort]
    generatorFunc = generator(data, 0)
    sortingUtils.colorAnim = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sortingUtils.sorting = not sortingUtils.sorting
        
        if sortingUtils.sorting:
            try:
                if sortingUtils.colorAnim is None:
                    next(generatorFunc)
                else:
                    next(sortingUtils.colorAnim)
            except StopIteration:
                if sortingUtils.colorAnim is None:
                        print("starting color anim")
                        sortingUtils.colorAnim = colorDataSet(data, len(data))
                else:
                    sortingUtils.colorAnim = None
                    sortingUtils.sorting = False

        SCREEN.fill("black")

        showDataToScreen(data)
        displayStats()
        pygame.display.flip()

if __name__ == "__main__":
    main()
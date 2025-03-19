import pygame
import random

pygame.init()

from sortingUtils import *
from bubbleSortAlgorithm import bubbleSort
from bogoSortAlgorithm import bogoSort

WIDTH, HEIGHT = 1280, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

data = []

def createTestData(length):
    for x in range(length):
        data.append(x + 1)
    
    random.shuffle(data)

createTestData(100)

def showDataToScreen(array):
    scaleFactor = (HEIGHT - 50) / max(array)
    SCREEN.fill("black")
    gap = WIDTH // len(array)
    for x in range(len(array)):
        rect = (x * gap, HEIGHT - (array[x] * scaleFactor), gap - 1, array[x] * scaleFactor)
        pygame.draw.rect(SCREEN, "white", rect)

def displayStats(swaps, comparisons):
    font = pygame.font.SysFont('Times New Roman', 20)
    stats_text = font.render(f"Swaps: {swaps} | Comparisons: {comparisons}", True, (255, 255, 255))
    SCREEN.fill("black", (10, 10, 1000, 30))
    SCREEN.blit(stats_text, (10, 10))

def main():
    running = True

    sortingAlgorithms = {
    "Bubble Sort": bubbleSort,
    "Bogo Sort": bogoSort,
    }

    selectedSort = "Bubble Sort"
    generator = sortingAlgorithms[selectedSort]
    generatorFunc = generator(data, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        next(generatorFunc)
                    except StopIteration:
                        pass
        SCREEN.fill("black")

        showDataToScreen(data)
        displayStats(swaps, comparisons)
        pygame.display.flip()

if __name__ == "__main__":
    main()
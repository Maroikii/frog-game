import pygame
import random

# Level 1 of the Frog Game

def run_level(screen):
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((120, 190, 120))
        pygame.display.flip()
        clock.tick(60)

    return "main_menu"
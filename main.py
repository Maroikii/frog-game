import sys
import pygame
import menu
import levels.level1 as level1


pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Frog Game")

    while True:
        action = menu.run_main_menu(screen)

        if action == "new_game":
            level1.run_level(screen)
        elif action == "continue_game":
            print("Continue game is not implemented yet.")
        elif action == "settings":
            print("Settings screen is not implemented yet.")
        elif action == "exit_game":
            break

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

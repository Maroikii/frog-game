import sys
import pygame
import asyncio

import menu
import levels.level1 as level1

async def main():
    pygame.init()

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Frog Game")

    while True:
        action = await menu.run_main_menu(screen)

        if action == "new_game":
            result = await level1.run_level(screen)
            if result == "quit":
                break
        elif action == "continue_game":
            print("Continue game is not implemented yet.")
        elif action == "settings":
            print("Settings screen is not implemented yet.")
        elif action == "exit_game":
            break
        
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    asyncio.run(main())
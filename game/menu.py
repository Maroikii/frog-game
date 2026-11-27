import sys
import pygame
import asyncio


WIDTH, HEIGHT = 1200, 800
BG_COLOR = (17, 24, 39)
PANEL_COLOR = (22, 38, 57)
BUTTON_COLOR = (34, 197, 94)
BUTTON_HOVER = (22, 163, 74)
BUTTON_TEXT = (240, 250, 255)
OUTLINE = (148, 163, 184)
TITLE_COLOR = (255, 255, 255)

async def menu():
    pygame.init()
    pygame.font.init()


    class Button:
        def __init__(self, text, x, y, width, height, action, color=BUTTON_COLOR,
                    hover_color=BUTTON_HOVER, text_color=BUTTON_TEXT):
            self.text = text
            self.action = action
            self.rect = pygame.Rect(x, y, width, height)
            self.color = color
            self.hover_color = hover_color
            self.text_color = text_color
            self.hovered = False

        def draw(self, screen, mouse_pos):
            self.hovered = self.rect.collidepoint(mouse_pos)
            color = self.hover_color if self.hovered else self.color
            pygame.draw.rect(screen, color, self.rect, border_radius=18)
            pygame.draw.rect(screen, OUTLINE, self.rect, 3, border_radius=18)

            font = pygame.font.SysFont("arial", 28, bold=True)
            label = font.render(self.text, True, self.text_color)
            screen.blit(label, label.get_rect(center=self.rect.center))

        def is_clicked(self, event):
            return (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.rect.collidepoint(event.pos)
            )


    class MainMenu:
        def __init__(self):
            self.title_font = pygame.font.SysFont("arial", 64, bold=True)
            self.buttons = [
                Button("NEW GAME", 475, 250, 250, 60, "new_game"),
                Button("CONTINUE GAME", 450, 340, 300, 60, "continue_game"),
                Button("SETTINGS", 495, 430, 210, 60, "settings"),
                Button("EXIT GAME", 500, 520, 200, 60, "exit_game", color=(239, 68, 68), hover_color=(220, 38, 38)),
            ]

        def draw(self, screen, mouse_pos):
            screen.fill(BG_COLOR)

            panel = pygame.Rect(330, 150, 540, 470)
            pygame.draw.rect(screen, PANEL_COLOR, panel, border_radius=30)
            pygame.draw.rect(screen, OUTLINE, panel, 3, border_radius=30)

            title = self.title_font.render("FROG GAME", True, TITLE_COLOR)
            screen.blit(title, title.get_rect(center=(WIDTH // 2, 95)))

            for button in self.buttons:
                button.draw(screen, mouse_pos)

        def handle_event(self, event):
            for button in self.buttons:
                if button.is_clicked(event):
                    return button.action
            return None


    def run_main_menu(screen):
        menu = MainMenu()
        clock = pygame.time.Clock()

        while True:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit_game"

                action = menu.handle_event(event)
                if action in {"new_game", "continue_game", "settings", "exit_game"}:
                    return action

            menu.draw(screen, mouse_pos)
            pygame.display.flip()
            clock.tick(60)

    def main():
        pygame.display.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Frog Game Menu")

        action = run_main_menu(screen)
        if action == "exit_game":
            pygame.quit()
            sys.exit()


    if __name__ == "__main__":
        main()
asyncio.run(menu())
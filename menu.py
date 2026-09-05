import sys
import pygame


WIDTH, HEIGHT = 900, 600
BG_COLOR = (17, 24, 39)
PANEL_COLOR = (22, 38, 57)
BUTTON_COLOR = (34, 197, 94)
BUTTON_HOVER = (22, 163, 74)
BUTTON_TEXT = (240, 250, 255)
OUTLINE = (148, 163, 184)
TITLE_COLOR = (255, 255, 255)

pygame.init()
pygame.font.init()


# Menu system for the Frog Game
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
    # Draw the button on the screen
    def draw(self, screen, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=18)
        pygame.draw.rect(screen, OUTLINE, self.rect, 3, border_radius=18)

        font = pygame.font.SysFont("arial", 28, bold=True)
        label = font.render(self.text, True, self.text_color)
        label_rect = label.get_rect(center=self.rect.center)
        screen.blit(label, label_rect)
    # Check if the button is clicked
    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )

# Main menu class for the Frog Game
class MainMenu:
    def __init__(self):
        self.title_font = pygame.font.SysFont("arial", 64, bold=True)
        self.sub_font = pygame.font.SysFont("arial", 18)
        self.buttons = [
            Button("NEW GAME", 325, 150, 250, 60, "new_game"),
            Button("CONTINUE GAME", 300, 240, 300, 60, "continue_game"),
            Button("SETTINGS", 345, 330, 210, 60, "settings"),
            Button("EXIT GAME", 350, 420, 200, 60, "exit_game", color=(239, 68, 68), hover_color=(220, 38, 38)),
        ]

    # Draw the main menu on the screen
    def draw(self, screen, mouse_pos):
        screen.fill(BG_COLOR)

        panel = pygame.Rect(180, 80, 540, 470)
        pygame.draw.rect(screen, PANEL_COLOR, panel, border_radius=30)
        pygame.draw.rect(screen, OUTLINE, panel, 3, border_radius=30)

        title = self.title_font.render("FROG GAME", True, TITLE_COLOR)
        title_rect = title.get_rect(center=(WIDTH // 2, 95))
        screen.blit(title, title_rect)

        subtitle = self.sub_font.render("Choose an option", True, (203, 213, 225))
        subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, 120))
        screen.blit(subtitle, subtitle_rect)

        for button in self.buttons:
            button.draw(screen, mouse_pos)

    def handle_event(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                return button.action
        return None


# Functions for handling menu actions
def new_game():
    print("Starting a new game...")
    return "new_game"


def continue_game():
    print("Continuing saved game...")
    return "continue_game"


def open_settings():
    print("Opening settings...")
    return "settings"


def exit_game():
    print("Exiting game...")
    return "exit_game"


def run_main_menu(screen):
    menu = MainMenu()
    clock = pygame.time.Clock()

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit_game"

            action = menu.handle_event(event)
            if action == "new_game":
                new_game()
                return "new_game"
            elif action == "continue_game":
                continue_game()
                return "continue_game"
            elif action == "settings":
                open_settings()
                return "settings"
            elif action == "exit_game":
                exit_game()
                return "exit_game"

        menu.draw(screen, mouse_pos)
        pygame.display.flip()
        clock.tick(60)


# Main function to run the menu
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

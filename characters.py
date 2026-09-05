import pygame


def draw_frog(screen, x, y, radius, body_color=(40, 160, 60), eye_color=(255, 255, 255), pupil_color=(0, 0, 0)):
    pygame.draw.circle(screen, body_color, (int(x), int(y)), int(radius))
    pygame.draw.circle(screen, eye_color, (int(x) - 15, int(y) - 20), 10)
    pygame.draw.circle(screen, eye_color, (int(x) + 15, int(y) - 20), 10)
    pygame.draw.circle(screen, pupil_color, (int(x) - 15, int(y) - 20), 5)
    pygame.draw.circle(screen, pupil_color, (int(x) + 15, int(y) - 20), 5)


def draw_fly(screen, x, y, radius, color=(30, 30, 30), wing_color=(200, 200, 200)):
    pygame.draw.circle(screen, color, (int(x), int(y)), int(radius))
    pygame.draw.circle(screen, wing_color, (int(x) - 7, int(y) - 6), 5)
    pygame.draw.circle(screen, wing_color, (int(x) + 7, int(y) - 6), 5)

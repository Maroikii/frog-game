import pygame
import random


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frida frosk")
running = True

# Vi lager Frode frosk

frog_x = SCREEN_WIDTH // 2
frog_y = SCREEN_HEIGHT // 2
frog_radius = 30
frog_speed = 3

clock = pygame.time.Clock()

# Frikk flue
fly_x = random.randint(30, SCREEN_WIDTH - 30)
fly_y = random.randint(30, SCREEN_HEIGHT - 30)
fly_radius = 8

# Vi lager spillet
score = 0
font = pygame.font.Font(None, 36)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # 1. Get the pressed keys state
    keys = pygame.key.get_pressed()

    # 2. Create a direction vector based on inputs
    move_x = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
    move_y = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])

    move_vector = pygame.math.Vector2(move_x, move_y)

    # 3. Normalize if moving to keep speed consistent
    speed = 5
    if move_vector.length_squared() > 0:
        move_vector.scale_to_length(speed)
        frog_x += move_vector.x
        frog_y += move_vector.y



    distance_x = frog_x - fly_x
    distance_y = frog_y - fly_y

    distance = (distance_x ** 2 + distance_y ** 2 ) ** 0.5

    if distance <= frog_radius + fly_radius:
        score += 1
        fly_x = random.randint(30, SCREEN_WIDTH - 30)
        fly_y = random.randint(30, SCREEN_HEIGHT - 30)

    screen.fill((120,190,120))

    pygame.draw.circle(screen, (40, 160, 60), (frog_x, frog_y), frog_radius)  # Frog body
    pygame.draw.circle(screen, (255, 255, 255), (frog_x - 15, frog_y - 20), 10)  # Left eye
    pygame.draw.circle(screen, (255, 255, 255), (frog_x + 15, frog_y - 20), 10)  # Right eye
    pygame.draw.circle(screen, (0, 0, 0), (frog_x - 15, frog_y - 20), 5)  # Left pupil
    pygame.draw.circle(screen, (0, 0, 0), (frog_x + 15, frog_y - 20), 5)  # Right pupil
    pygame.draw.circle(screen, (30, 30, 30), (fly_x, fly_y), fly_radius)  # Fly
    pygame.draw.circle(screen, (200, 200, 200), (fly_x - 7, fly_y - 6), 5)  # Left wing
    pygame.draw.circle(screen, (200, 200, 200), (fly_x + 7, fly_y - 6), 5)  # Right wing

    score_text = font.render(f"Fluer spist: {score}", True, (30, 30, 30))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

    #grow when fly is eaten
    frog_radius = 30 + score // 1

    # Keep the frog within the screen boundaries
    frog_x = max(frog_radius, min(SCREEN_WIDTH - frog_radius, frog_x))
    frog_y = max(frog_radius, min(SCREEN_HEIGHT - frog_radius, frog_y)) 

    # if the frog gets too big, explode frog and reset the game
    if frog_radius >= 50:
        frog_radius = 30
        score = 0

        pygame.draw.circle(screen, (255, 0, 0), (frog_x, frog_y), frog_radius)  # Draw the exploded frog
        pygame.display.flip()

        game_over_text = font.render("Frosken eksploderte! Trykk på 'R' for å starte på nytt.", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()

        waiting_for_restart = True

        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_restart = False
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    waiting_for_restart = False
                    frog_x = SCREEN_WIDTH // 2
                    frog_y = SCREEN_HEIGHT // 2
                    fly_x = random.randint(30, SCREEN_WIDTH - 30)
                    fly_y = random.randint(30, SCREEN_HEIGHT - 30)
                    score = 0

pygame.quit()
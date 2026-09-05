import random
import pygame

# Level 1 of the Frog Game

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600


def run_level(screen):
    pygame.display.set_caption("Frog Game - Level 1")

    frog_x = SCREEN_WIDTH // 2
    frog_y = SCREEN_HEIGHT // 2
    frog_radius = 30

    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.Font(None, 36)

    fly_x = random.randint(30, SCREEN_WIDTH - 30)
    fly_y = random.randint(30, SCREEN_HEIGHT - 30)
    fly_radius = 8

    red_fly_x = random.randint(30, SCREEN_WIDTH - 30)
    red_fly_y = random.randint(30, SCREEN_HEIGHT - 30)
    red_fly_radius = 8

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return "quit"

        keys = pygame.key.get_pressed()
        move_x = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
        move_y = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])

        move_vector = pygame.math.Vector2(move_x, move_y)

        speed = 5
        if move_vector.length_squared() > 0:
            move_vector.scale_to_length(speed)
            frog_x += move_vector.x
            frog_y += move_vector.y

        distance_x = frog_x - fly_x
        distance_y = frog_y - fly_y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        if distance <= frog_radius + fly_radius:
            score += 1
            fly_x = random.randint(30, SCREEN_WIDTH - 30)
            fly_y = random.randint(30, SCREEN_HEIGHT - 30)

        distance_red_fly_x = frog_x - red_fly_x
        distance_red_fly_y = frog_y - red_fly_y
        distance_red_fly = (distance_red_fly_x ** 2 + distance_red_fly_y ** 2) ** 0.5

        if distance_red_fly <= frog_radius + red_fly_radius:
            score += 2
            red_fly_x = random.randint(30, SCREEN_WIDTH - 30)
            red_fly_y = random.randint(30, SCREEN_HEIGHT - 30)

        screen.fill((120, 190, 120))

        pygame.draw.circle(screen, (40, 160, 60), (frog_x, frog_y), frog_radius)
        pygame.draw.circle(screen, (255, 255, 255), (frog_x - 15, frog_y - 20), 10)
        pygame.draw.circle(screen, (255, 255, 255), (frog_x + 15, frog_y - 20), 10)
        pygame.draw.circle(screen, (0, 0, 0), (frog_x - 15, frog_y - 20), 5)
        pygame.draw.circle(screen, (0, 0, 0), (frog_x + 15, frog_y - 20), 5)

        pygame.draw.circle(screen, (30, 30, 30), (fly_x, fly_y), fly_radius)
        pygame.draw.circle(screen, (200, 200, 200), (fly_x - 7, fly_y - 6), 5)
        pygame.draw.circle(screen, (200, 200, 200), (fly_x + 7, fly_y - 6), 5)

        pygame.draw.circle(screen, (255, 0, 0), (red_fly_x, red_fly_y), red_fly_radius)
        pygame.draw.circle(screen, (200, 200, 200), (red_fly_x - 7, red_fly_y - 6), 5)
        pygame.draw.circle(screen, (200, 200, 200), (red_fly_x + 7, red_fly_y - 6), 5)

        score_text = font.render(f"Fluer spist: {score}", True, (30, 30, 30))
        screen.blit(score_text, (10, 10))

        frog_radius = 30 + score // 1
        frog_x = max(frog_radius, min(SCREEN_WIDTH - frog_radius, frog_x))
        frog_y = max(frog_radius, min(SCREEN_HEIGHT - frog_radius, frog_y))

        if frog_radius >= 100:
            pygame.draw.circle(screen, (255, 0, 0), (frog_x, frog_y), frog_radius)
            pygame.display.flip()
            pygame.time.wait(1000)

            frog_x = SCREEN_WIDTH // 2
            frog_y = SCREEN_HEIGHT // 2
            frog_radius = 30
            score = 0

            game_over_text = font.render("Frosken eksploderte! Trykk på 'R' for å starte på nytt.", True, (0, 0, 0))
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
            pygame.display.flip()

            waiting_for_restart = True
            while waiting_for_restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting_for_restart = False
                        running = False
                        return "quit"
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        waiting_for_restart = False
                        frog_x = SCREEN_WIDTH // 2
                        frog_y = SCREEN_HEIGHT // 2
                        fly_x = random.randint(30, SCREEN_WIDTH - 30)
                        fly_y = random.randint(30, SCREEN_HEIGHT - 30)
                        score = 0

        pygame.display.flip()
        clock.tick(60)

    return "quit"
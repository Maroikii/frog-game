import math
import random
import asyncio
import pygame

from characters import draw_frog, draw_fly


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BG_COLOR = (120, 190, 120)
TEXT_COLOR = (30, 30, 30)


async def pause_menu(screen, font, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
    pause_text = font.render("Paused. Press 'ESC' to resume.", True, (0, 0, 0)) 
    text_rect = pause_text.get_rect(center=(width // 2, height // 2))
    screen.blit(pause_text, text_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "resume"
        
        await asyncio.sleep(0)


def spawn_fly(width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
    return (
        random.randint(30, width - 30),
        random.randint(30, height - 30),
    )


def move_frog(frog_x, frog_y, keys, speed=5):
    move_x = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT]) 
    move_y = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])

    move_vector = pygame.math.Vector2(move_x, move_y)
    if move_vector.length_squared() > 0:
        move_vector.scale_to_length(speed)
        frog_x += move_vector.x
        frog_y += move_vector.y

    return frog_x, frog_y


async def run_level(screen, level_name="Level 1", background_color=BG_COLOR, text_color=TEXT_COLOR):
    pygame.display.set_caption(f"Frog Game - {level_name}")

    frog_x = SCREEN_WIDTH // 2
    frog_y = SCREEN_HEIGHT // 2
    frog_radius = 30

    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.Font(None, 36)

    fly_x, fly_y = spawn_fly()
    red_fly_x, red_fly_y = spawn_fly()
    fly_radius = 8
    red_fly_radius = 8

    running = True
    while running:
        screen.fill(background_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            action = await pause_menu(screen, font)
            if action == "quit":
                return "quit"

        frog_x, frog_y = move_frog(frog_x, frog_y, keys)

        fly_distance = math.hypot(frog_x - fly_x, frog_y - fly_y)
        if fly_distance <= frog_radius + fly_radius:
            score += 1
            fly_x, fly_y = spawn_fly()

        red_fly_distance = math.hypot(frog_x - red_fly_x, frog_y - red_fly_y)
        if red_fly_distance <= frog_radius + red_fly_radius:
            score += 2
            red_fly_x, red_fly_y = spawn_fly()

        level_text = font.render(level_name, True, text_color)
        screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, 10))

        draw_frog(screen, frog_x, frog_y, frog_radius)
        draw_fly(screen, fly_x, fly_y, fly_radius)
        draw_fly(screen, red_fly_x, red_fly_y, red_fly_radius, color=(255, 0, 0))

        score_text = font.render(f"Fluer spist: {score}", True, text_color)
        screen.blit(score_text, (10, 10))

        frog_radius = 30 + score
        frog_x = max(frog_radius, min(SCREEN_WIDTH - frog_radius, frog_x))
        frog_y = max(frog_radius, min(SCREEN_HEIGHT - frog_radius, frog_y))

        if frog_radius >= 100:
            pygame.draw.circle(screen, (255, 0, 0), (int(frog_x), int(frog_y)), int(frog_radius))
            pygame.display.flip()
            await asyncio.sleep(1)

            frog_x = SCREEN_WIDTH // 2
            frog_y = SCREEN_HEIGHT // 2
            frog_radius = 30
            score = 0
            fly_x, fly_y = spawn_fly()
            red_fly_x, red_fly_y = spawn_fly()

            game_over_text = font.render("Frosken eksploderte! Trykk på 'R' for å starte på nytt.", True, (0, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(game_over_text, game_over_rect)
            pygame.display.flip()

            waiting_for_restart = True
            while waiting_for_restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return "quit"
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        waiting_for_restart = False
                        frog_x = SCREEN_WIDTH // 2
                        frog_y = SCREEN_HEIGHT // 2
                        fly_x, fly_y = spawn_fly()
                        red_fly_x, red_fly_y = spawn_fly()
                        score = 0
                
                await asyncio.sleep(0)

        pygame.display.flip()
        clock.tick(60)
        
        await asyncio.sleep(0)
        clock.tick(60)

    return "quit"
import pygame
import random
import time
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch 67")

font = pygame.font.SysFont(None, 50)

def draw_text(text, x, y):
    img = font.render(text, True, (255,255,255))
    screen.blit(img, (x, y))


def game():
    player = pygame.Rect(250, 350, 80, 30)
    falling = pygame.Rect(random.randint(0, 550), 0, 50, 50)

    speed = 7
    fall_speed = 5
    score = 0
    start_time = time.time()

    r, g, b = 0, 0, 0

    running = True
    while running:
        pygame.time.delay(20)

        elapsed = time.time() - start_time
        if elapsed > 30:
            break

        fall_speed = 5 + int(elapsed / 5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed

        falling.y += fall_speed
        if falling.y > height:
            falling.y = 0
            falling.x = random.randint(0, 550)

        if player.colliderect(falling):
            score += 1
            falling.y = 0
            falling.x = random.randint(0, 550)

       
        r = (r + 1) % 256
        g = (g + 2) % 256
        b = (b + 3) % 256
        screen.fill((r, g, b))

        pygame.draw.rect(screen, (0,255,0), player)

        text_67 = font.render("67", True, (255,255,255))
        screen.blit(text_67, (falling.x, falling.y))

        draw_text(f"Score: {score}", 10, 10)

        pygame.display.update()

    return score


def menu():
    while True:
        screen.fill((0,0,0))

        draw_text("Catch 67", 200, 80)
        draw_text("Press ENTER to Start", 120, 180)
        draw_text("Press ESC to Quit", 140, 240)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score = game()
                    end_screen(score)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def end_screen(score):
    while True:
        screen.fill((0,0,0))

        draw_text(f"Score: {score}", 200, 120)
        draw_text("six seven is good ", 60, 180)
        draw_text("Press R to Restart", 130, 250)
        draw_text("Press ESC to Menu", 120, 300)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    score = game()
                if event.key == pygame.K_ESCAPE:
                    return

menu()
import pygame
import time

WHITE = (255, 255, 255)
RED = (255, 0, 0)

crosshair_img = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.circle(crosshair_img, RED, (25, 25), 25, 2)
pygame.draw.line(crosshair_img, RED, (25, 0), (25, 50), 2)
pygame.draw.line(crosshair_img, RED, (0, 25), (50, 25), 2)

can_shoot = True
last_shot_time = 0

def draw_crosshair(screen, x, y):
    screen.blit(crosshair_img, (x - 25, y - 25))

def handle_shooting(event, screen):
    global can_shoot, last_shot_time

    if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
        can_shoot = False
        last_shot_time = time.time()
        mouse_x, mouse_y = event.pos
        draw_crosshair(screen, mouse_x, mouse_y)
        pygame.display.flip()

    if not can_shoot and time.time() - last_shot_time >= 3:
        can_shoot = True

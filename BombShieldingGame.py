import random

import pygame

color_white = [255,255,255]
color_of_background = [98,95,99]
color_of_bomb = [187,189,246]
color_of_player = [121,122,158]

pygame.init()

size_of_screen = [800, 600]
size_of_player = [100, 20]
size_of_bomb = 30

font_size_20 = pygame.font.Font('gomarice_g_type.ttf', 20)
main_screen = pygame.display.set_mode(size_of_screen)
pygame.display.set_caption("Bomb Shielding Game - Dhruv")

def write_text(text_to_draw, horizontal_position, vertical_position, color):
    text_to_draw = font_size_20.render(text_to_draw, True, color)
    main_screen.blit(text_to_draw, [horizontal_position, vertical_position])

closing = False
clock = pygame.time.Clock()
position_of_player = [10, size_of_screen[1] - size_of_player[1]]
position_of_bomb = [random.randint(0, size_of_screen[0]), 0]
num_lives = 3
num_points = 0

while not closing and num_lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closing = True
    main_screen.fill(color_of_background)

    list_of_keys = pygame.key.get_pressed()
    if list_of_keys[pygame.K_LEFT]:
        position_of_player[0] += -5
    if list_of_keys[pygame.K_RIGHT]:
        position_of_player[0] += 5

    position_of_bomb[1] += 4
    
    bomb_rectangle = pygame.draw.circle(main_screen, color_of_bomb, position_of_bomb, size_of_bomb)
    player_rectangle = pygame.draw.rect(main_screen, color_of_player, [position_of_player[0], position_of_player[1], size_of_player[0], size_of_player[1]])

    if player_rectangle.colliderect(bomb_rectangle):
        position_of_bomb = [random.randint(0, size_of_screen[0]), 0]
        num_points += 10
    
    if position_of_bomb[1] >= size_of_screen[1]:
        position_of_bomb = [random.randint(0, size_of_screen[0]), 0]
        num_lives += - 1

    write_text(f"{num_lives} lives left", 5, 5, color_white)
    write_text(f"you have {num_points} points", size_of_screen[0] - 300, 5, color_white)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
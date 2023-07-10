import pygame
from board import boards


pygame.init()


WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)


def draw_board(lvl):
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):



run = True

while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
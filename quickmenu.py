import pygame
from pygame.locals import *
from sys import exit
from random import *
import os

main_dir = os.path.dirname(__file__)
img_dir = os.path.join(main_dir, 'imagens')
font_dir = os.path.join(main_dir, 'fontes')

pygame.init()

# Largura e Altura da Página
w = 1000
h = 750

# Inicializando tela, plano de fundo e sprites que vão aparecer na tela
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
font = pygame.font.Font(os.path.join(font_dir ,'rudiment.ttf'), 100)

initgame = False

difficult = 2

# MENU DO JOGO
while True:
    screen.fill((255, 255, 255))

    # Recebe a posição do mouse na tela
    mx, my = pygame.mouse.get_pos()
    loc = [mx, my]
    click = []

    # Recebe inputs de Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            click = loc
            click_area = pygame.draw.rect(screen, (0,0,0), (click[0], click[1], 10, 10))
            print(click)

    pygame.display.flip()
    clock.tick(60)
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
w = 900
h = 675

# Inicializando tela, plano de fundo e sprites que vão aparecer na tela
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
font = pygame.font.Font(os.path.join(font_dir ,'rudiment.ttf'), 100)

menuspritesheet = pygame.image.load(os.path.join(img_dir, 'menuSpritesheet.png')).convert_alpha()
arrowlist1 = ((0,200), (200,200))
arrowlist2 = ((100,200),(300,200))
class Init(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.init = False
        self.image = menuspritesheet.subsurface((0, 0), (400, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (450, 100)
class Difficult(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = menuspritesheet.subsurface((0, 100), (400, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (450, 300)
class Arrow1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animate = False
        self.index = 0
        self.image = menuspritesheet.subsurface(arrowlist1[self.index], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (250, 310)

    def select(self):
        self.animate = True

    def update(self):
        if self.animate == True:
            self.index += 0.5
            if self.index >= len(arrowlist1):
                self.index = 0
                self.animate = False
            self.image = menuspritesheet.subsurface(arrowlist1[int(self.index)], (100, 100))
class Arrow2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animate = False
        self.index = 0
        self.image = menuspritesheet.subsurface(arrowlist2[self.index], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (650, 310)

    def select(self):
        self.animate = True

    def update(self):
        if self.animate == True:
            self.index += 0.5
            if self.index >= len(arrowlist2):
                self.index = 0
                self.animate = False
            self.image = menuspritesheet.subsurface(arrowlist2[int(self.index)], (100, 100))

difficult_list = ((400, 200), (0, 300), (400, 300))
class DifficultSet(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.difficult = 0
        self.image = menuspritesheet.subsurface(difficult_list[self.difficult], (400, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (450, 400)

    def difficultDecrease(self):
        if self.difficult == 0:
            pass
        else:
            arrow1.select()
            self.difficult -= 1
            self.image = menuspritesheet.subsurface(difficult_list[self.difficult], (400, 100))
    def difficultIncrease(self):
        if self.difficult == 2:
            pass
        else:
            arrow2.select()
            self.difficult += 1
            self.image = menuspritesheet.subsurface(difficult_list[self.difficult], (400, 100))

all_menu_sprites = pygame.sprite.Group()
initgame = Init()
difficult = Difficult()
difficult_set = DifficultSet()
arrow1 = Arrow1()
arrow2 = Arrow2()

all_menu_sprites.add(initgame, difficult, difficult_set, arrow1, arrow2)

# MENU DO JOGO
while initgame.init == False:
    screen.fill((255, 255, 255))
    print(arrow1.index)
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

    all_menu_sprites.draw(screen)

    if len(click) > 0:

        if click_area.colliderect(initgame.rect):
            initgame.init = True

        elif click_area.colliderect(arrow1.rect):
            difficult_set.difficultDecrease()
                            
        elif click_area.colliderect(arrow2.rect):
            difficult_set.difficultIncrease()
                
    arrow1.update()
    arrow2.update()
    pygame.display.flip()
    clock.tick(60)
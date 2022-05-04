import pygame
from pygame.locals import *
from sys import exit
from random import *
import os

main_dir = os.path.dirname(__file__)
img_dir = os.path.join(main_dir, 'imagens')
font_dir = os.path.join(main_dir, 'fontes')

pygame.init()

w = 1000
h = 750

i_cont = []
img_pos = [(480, 100), (480, 320), (480, 620), (660, 100), (660, 320), (660, 620), (900, 100), (900, 320), (900, 620)]
random_img_pos = []
for p in range (len(img_pos)):
    i = randint(0, len(img_pos)-1)
    i_cont.append(i)

    while (i_cont.count(i) > 1):
        i_cont.pop()
        i = randint(0, len(img_pos)-1)
        i_cont.append(i)
    random_img_pos.append(img_pos[i]) 

random_words = []
random_sprites = []

easy_words = ('Car', 'Apple', 'Cellphone', 'House', 'Class', 'Door', 'Bike', 'Computer', 'Teacher')

font = pygame.font.Font(os.path.join(font_dir ,'rudiment.ttf'), 50)
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Word Game - Aprendendo Inglês')
clock = pygame.time.Clock()
random_list = True

background = pygame.image.load(os.path.join(img_dir, 'wordgame_bg.jpg')).convert()
spritesheet = pygame.image.load(os.path.join(img_dir, 'wordgameSpritesheet.png')).convert_alpha()

class MouseCursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((0, 300), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.image = pygame.transform.scale(self.image, (50, 50))

    def cursor_pos(self, loc):
        self.rect.center = (loc[0]+50,loc[1]+50)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((0, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[0])

    def change_ss(self):
        self.image = spritesheet.subsurface((0, 100), (100, 100))

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((100, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[1])

    def change_ss(self):
        self.image = spritesheet.subsurface((100, 100), (100, 100))

class Cellphone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((200, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[2])

    def change_ss(self):
        self.image = spritesheet.subsurface((200, 100), (100, 100))

class House(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((300, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[3])

    def change_ss(self):
        self.image = spritesheet.subsurface((300, 100), (100, 100))

class Classe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((400, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[4])

    def change_ss(self):
        self.image = spritesheet.subsurface((400, 100), (100, 100))

class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((500, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[5])

    def change_ss(self):
        self.image = spritesheet.subsurface((500, 100), (100, 100))

class Bike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((600, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[6])

    def change_ss(self):
        self.image = spritesheet.subsurface((600, 100), (100, 100))

class Computer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((700, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[7])

    def change_ss(self):
        self.image = spritesheet.subsurface((700, 100), (100, 100))

class Teacher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((800, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[8])
        
    def change_ss(self):
        self.image = spritesheet.subsurface((800, 100), (100, 100))


cursor = MouseCursor()
cursor_sprite = pygame.sprite.Group()
cursor_sprite.add(cursor)
all_sprites = pygame.sprite.Group()
car = Car()
apple = Apple()
cellphone = Cellphone()
house = House()
classe = Classe()
door = Door()
bike = Bike()
computer = Computer()
teacher = Teacher()
lista_sprites = [car, apple, cellphone, house, classe, door, bike, computer, teacher]
click_area = pygame.draw.rect(screen, (0,0,0), (0, 0, 20, 20))
while True:
    clock.tick(60)
    screen.fill((255, 255, 255))

    mx, my = pygame.mouse.get_pos()
    loc = [mx, my]
    click = []
    cursor.cursor_pos(loc)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            click = loc
            click_area = pygame.draw.rect(screen, (0,0,0), (click[0], click[1], 10, 10))
            print(click)       
            
    # CONTEÚDO EXIBIDO À ESQUERDA ------------------------------------------------------- #

    # Armazena randomicamente um item da lista de palavras numa nova lista, que será utilizada para exibir as palavras na tela
    i_cont = []
    if random_list == True:
        random_list = False
        for w in range (0,4):
            i = randint(0, (len(easy_words)-1))
            i_cont.append(i)

            # Previne que o algoritmo gere índices repetidos ---------------------------------#
            while (i_cont.count(i) > 1):
                i_cont.pop()
                i = randint(0, (len(easy_words)-1))
                i_cont.append(i)

            random_words.append(easy_words[i])
            random_sprites.append(lista_sprites[i])
        all_sprites.add(random_sprites)
        print(random_sprites)

    # Diz como será exibida cada uma das palavras na tela --------------------------------#
    ftext1 = font.render(random_words[0], True, (255, 255, 255))
    txtbox1 = ftext1.get_rect()
    txtbox1 = (50, 50)

    ftext2 = font.render(random_words[1], True, (255, 255, 255))
    txtbox2 = ftext2.get_rect()
    txtbox2 = (50, 170)

    ftext3 = font.render(random_words[2], True, (255, 255, 255))
    txtbox3 = ftext3.get_rect()
    txtbox3 = (50, 290)

    ftext4 = font.render(random_words[3], True, (255, 255, 255))
    txtbox4 = ftext4.get_rect()
    txtbox4 = (50, 410)
    
    # Exibe elementos na tela -----------------------------------#
    screen.blit(background, (0,0))
    screen.blit(ftext1, txtbox1)
    screen.blit(ftext2, txtbox2)
    screen.blit(ftext3, txtbox3)
    screen.blit(ftext4, txtbox4)
    all_sprites.draw(screen)
    cursor_sprite.draw(screen)
    
    # Colisões e alteração de estado ----------------------------#
    if len(click) > 0:
        if click_area.colliderect(car.rect):
            car.change_ss()

        elif click_area.colliderect(apple.rect):
            apple.change_ss()

        elif click_area.colliderect(cellphone.rect):
            cellphone.change_ss()

        elif click_area.colliderect(house.rect):
            house.change_ss()

        elif click_area.colliderect(classe.rect):
            classe.change_ss()

        elif click_area.colliderect(door.rect):
            door.change_ss()

        elif click_area.colliderect(bike.rect):
            bike.change_ss()

        elif click_area.colliderect(computer.rect):
            computer.change_ss()

        elif click_area.colliderect(teacher.rect):
            teacher.change_ss()

        else:
            pass
    pygame.display.flip()
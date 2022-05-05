import pygame
from pygame.locals import *
from sys import exit
from random import *
import os

# Seta o diretório absoluto do jogo e subpastas
main_dir = os.path.dirname(__file__)
img_dir = os.path.join(main_dir, 'imagens')
font_dir = os.path.join(main_dir, 'fontes')

pygame.init()

# Largura e Altura da Página
w = 1000
h = 750

# Algoritmo para randomizar a posição das palavras na tela
i_cont = []
word_pos = [(50, 50), (50, 170), (50, 290), (50, 410), (50, 530), (50, 650)]
random_word_pos = []
for p in range (len(word_pos)):
    i = randint(0, len(word_pos)-1)
    i_cont.append(i)

    while (i_cont.count(i) > 1):
        i_cont.pop()
        i = randint(0, len(word_pos)-1)
        i_cont.append(i)
    random_word_pos.append(word_pos[i])

# Algoritmo para randomizar a posição das imagens na tela    
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

# Lista de Palavras (PROVISÓRIO)
easy_words = ('Car', 'Apple', 'Cellphone', 'House', 'Class', 'Door', 'Bike', 'Computer', 'Teacher')

# Fonte das Palavras (PROVISÓRIO MAS PODE TER USO DEPOIS)
font = pygame.font.Font(os.path.join(font_dir ,'rudiment.ttf'), 50)

# Inicializando tela, plano de fundo e sprites que vão aparecer na tela
screen = pygame.display.set_mode((w,h))
background = pygame.image.load(os.path.join(img_dir, 'wordgame_bg.jpg')).convert()
spritesheet1 = pygame.image.load(os.path.join(img_dir, 'objectSpritesheet.png')).convert_alpha()
spritesheet2 = pygame.image.load(os.path.join(img_dir, 'wordSpritesheet.png')).convert_alpha()

# Nome da Página, Utilização do Clock para definir FrameRate
pygame.display.set_caption('Word Game - Aprendendo Inglês')
clock = pygame.time.Clock()

# Variável que será utilizada para randomizar quais imagens aparecerão na tela
random_list = True

# Listas  de posições das Imagens dentro da Spritesheet -> subsurface
car_ss_xy = [(0,0), (0, 100), (0, 200)]
apple_ss_xy = [(100, 0), (100, 100), (100, 200)]
cellphone_ss_xy = [(200, 0), (200, 100), (200, 200)]
house_ss_xy = [(300, 0), (300, 100), (300, 200)]
classe_ss_xy = [(400, 0), (400, 100), (400, 200)]
door_ss_xy = [(500, 0), (500, 100), (500, 200)]
bike_ss_xy = [(600, 0), (600, 100), (600, 200)]
computer_ss_xy = [(700, 0), (700, 100), (700, 200)]
teacher_ss_xy = [(800, 0), (800, 100), (800, 200)]

# Cursor do Mouse (TESTE)
class MouseCursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet1.subsurface((0, 400), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.image = pygame.transform.scale(self.image, (50, 50))

    def cursor_pos(self, loc):
        self.rect.center = (loc[0]+50,loc[1]+50)

# Sprites dos Objetos
class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = 'Car'
        self.image = spritesheet1.subsurface(car_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[0])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet1.subsurface(car_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet1.subsurface(car_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = 'Apple'
        self.image = spritesheet1.subsurface(apple_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[1])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet1.subsurface(apple_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet1.subsurface(apple_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Cellphone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = 'Cellphone'
        self.image = spritesheet1.subsurface(cellphone_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[2])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet1.subsurface(cellphone_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet1.subsurface(cellphone_ss_xy[1], (100, 100))
        else:
            self.unselect()
class House(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = 'House'
        self.image = spritesheet1.subsurface(house_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[3])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet1.subsurface(house_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet1.subsurface(house_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Classe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = 'Classe'
        self.image = spritesheet1.subsurface(classe_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[4])
        self.selected = False
    
    def unselect(self):
        self.selected = False
        self.image = spritesheet1.subsurface(classe_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet1.subsurface(classe_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = 'Door'
        self.image = spritesheet1.subsurface((500, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[5])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet1.subsurface(door_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet1.subsurface(door_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Bike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = 'Bike'
        self.image = spritesheet1.subsurface((600, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[6])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet1.subsurface(bike_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet1.subsurface(bike_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Computer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = 'Computer'
        self.image = spritesheet1.subsurface((700, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[7])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet1.subsurface(computer_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet1.subsurface(computer_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Teacher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = 'Teacher'
        self.image = spritesheet1.subsurface((800, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[8])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet1.subsurface(teacher_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet1.subsurface(teacher_ss_xy[1], (100, 100))
        else:
            self.unselect()
def unselect_all():
    car.unselect()
    apple.unselect()
    cellphone.unselect()
    house.unselect()
    classe.unselect()
    door.unselect()
    bike.unselect()
    computer.unselect()
    teacher.unselect()

# Sprites das Palavras (TERMINAR)
'''class CarWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__inite__(self)
        self.word = 'Car'
        self.image = spritesheet1.subsurface(carword_ss_xy, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[0])
        self.selected = False'''

# Instanciando Classes de Sprites
# Mouse
cursor = MouseCursor()
cursor_sprite = pygame.sprite.Group()
cursor_sprite.add(cursor)
# Imagens de Objetos
all_object_sprites = pygame.sprite.Group()
car = Car()
apple = Apple()
cellphone = Cellphone()
house = House()
classe = Classe()
door = Door()
bike = Bike()
computer = Computer()
teacher = Teacher()
# Lista que será usada para randomizar quais objetos aparecerá na tela
lista_img = [car, apple, cellphone, house, classe, door, bike, computer, teacher]
# Lista que será usada para randomizar quais palavras aparecerá na tela
'''lista_words = [carw, applew,]'''
word_index = []
img_index = []

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
            random_sprites.append(lista_imagens[i])
        all_object_sprites.add(random_sprites)

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
    all_object_sprites.draw(screen)
    cursor_sprite.draw(screen)
    
    # Colisões e alteração de estado ----------------------------#
    selected_list = [car.selected, apple.selected, cellphone.selected, house.selected, classe.selected, door.selected, bike.selected, computer.selected, teacher.selected]
    
    if len(click) > 0:
        if click_area.colliderect(car.rect):
            if selected_list.count(True) <= 1:
                car.change_ss()

        elif click_area.colliderect(apple.rect):
            if selected_list.count(True) <= 1:
                apple.change_ss()

        elif click_area.colliderect(cellphone.rect):
            if selected_list.count(True) <= 1:
                cellphone.change_ss()

        elif click_area.colliderect(house.rect):
            if selected_list.count(True) <= 1:
                house.change_ss()

        elif click_area.colliderect(classe.rect):
            if selected_list.count(True) <= 1:
                classe.change_ss()

        elif click_area.colliderect(door.rect):
            if selected_list.count(True) <= 1:
                door.change_ss()

        elif click_area.colliderect(bike.rect):
            if selected_list.count(True) <= 1:
                bike.change_ss()

        elif click_area.colliderect(computer.rect):
            if selected_list.count(True) <= 1:
                computer.change_ss()

        elif click_area.colliderect(teacher.rect):
            if selected_list.count(True) <= 1:
                teacher.change_ss()

    if selected_list.count(True) > 1:
        unselect_all()
    
    pygame.display.flip()
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
word_pos = [(30, 60), (30, 125), (30, 190), (30, 255), (30, 320), (30,385), (30, 450), (30, 515), (30, 580)]
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
lista_words = ('Car', 'Apple', 'Cellphone', 'House', 'Class', 'Door', 'Bike', 'Computer', 'Teacher')

# Fonte das Palavras (PROVISÓRIO MAS PODE TER USO DEPOIS)
font = pygame.font.Font(os.path.join(font_dir ,'rudiment.ttf'), 50)

# Inicializando tela, plano de fundo e sprites que vão aparecer na tela
screen = pygame.display.set_mode((w,h))
background = pygame.image.load(os.path.join(img_dir, 'wordgame_bg.jpg')).convert()
spritesheet = pygame.image.load(os.path.join(img_dir, 'objectSpritesheet.png')).convert_alpha()
spritesheet2 = pygame.image.load(os.path.join(img_dir, 'wordSpritesheet.png')).convert_alpha()

# Nome da Página, Utilização do Clock para definir FrameRate
pygame.display.set_caption('Word Game - Aprendendo Inglês')
clock = pygame.time.Clock()

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

# Listas  de posições das Palavras dentro da Spritesheet -> subsurface
carword_ss_xy = [(0,0), (200, 0), (400, 0)]
appleword_ss_xy = [(0, 60), (200, 60), (400, 60)]
cellphoneword_ss_xy = [(0, 120), (200, 120), (400, 120)]
houseword_ss_xy = [(0, 180), (200, 180), (400, 180)]
classeword_ss_xy = [(0, 240), (200, 240), (400, 240)]
doorword_ss_xy = [(0, 300), (200, 300), (400, 300)]
bikeword_ss_xy = [(0, 360), (200, 360), (400, 360)]
computerword_ss_xy = [(0, 420), (200, 420), (400, 420)]
teacherword_ss_xy = [(0, 480), (200, 480), (400, 480)]

# Variável que será utilizada para determinar que as spritesheets só serão randomizadas uma ves (Será False depois que o loop for percorrido pela primeira vez)
random_list = True

# Cursor do Mouse (TESTE)
class MouseCursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((0, 400), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.image = pygame.transform.scale(self.image, (50, 50))

    def cursor_pos(self, loc):
        self.rect.center = (loc[0]+50,loc[1]+50)

# Sprites dos Objetos
class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Car'
        self.image = spritesheet.subsurface(car_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[0])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(car_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(car_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Apple'
        self.image = spritesheet.subsurface(apple_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[1])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(apple_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(apple_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Cellphone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Cellphone'
        self.image = spritesheet.subsurface(cellphone_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[2])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(cellphone_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(cellphone_ss_xy[1], (100, 100))
        else:
            self.unselect()
class House(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'House'
        self.image = spritesheet.subsurface(house_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[3])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(house_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(house_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Classe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Classe'
        self.image = spritesheet.subsurface(classe_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[4])
        self.selected = False
    
    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(classe_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(classe_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Door'
        self.image = spritesheet.subsurface((500, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[5])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(door_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(door_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Bike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Bike'
        self.image = spritesheet.subsurface((600, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[6])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(bike_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(bike_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Computer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Computer'
        self.image = spritesheet.subsurface((700, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[7])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(computer_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(computer_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Teacher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Teacher'
        self.image = spritesheet.subsurface((800, 0), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[8])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(teacher_ss_xy[0], (100, 100))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(teacher_ss_xy[1], (100, 100))
        else:
            self.unselect()

# Sprites das Palavras (TERMINAR)
class CarWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Car'
        self.image = spritesheet.subsurface(carword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[0])
        self.selected = False
    
    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(carword_ss_xy[0], (200,60))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(carword_ss_xy[1], (200,60))
        else:
            self.unselect()
class AppleWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Apple'
        self.image = spritesheet.subsurface(appleword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[1])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(appleword_ss_xy[0], (200,60))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(appleword_ss_xy[1], (200,60))
        else:
            self.unselect()
class CellphoneWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Cellphone'
        self.image = spritesheet.subsurface(cellphoneword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[2])
        self.selected = False
    
    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(cellphoneword_ss_xy[0], (200,60))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(cellphoneword_ss_xy[1], (200,60))
        else:
            self.unselect()
class HouseWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'House'
        self.image = spritesheet.subsurface(houseword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[3])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(houseword_ss_xy[0], (200,60))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(houseword_ss_xy[1], (200,60))
        else:
            self.unselect()
class ClasseWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Classe'
        self.image = spritesheet.subsurface(classeword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[4])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(classeword_ss_xy[0], (200,60))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(classeword_ss_xy[1], (200,60))
        else:
            self.unselect()
class DoorWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Door'
        self.image = spritesheet.subsurface(doorword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[5])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(doorword_ss_xy[0], (200,60))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(doorword_ss_xy[1], (200,60))
        else:
            self.unselect()
class BikeWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Bike'
        self.image = spritesheet.subsurface(bikeword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[6])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(bikeword_ss_xy[0], (200,60))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(bikeword_ss_xy[1], (200,60))
        else:
            self.unselect()
class ComputerWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Computer'
        self.image = spritesheet.subsurface(computerword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[7])
        self.selected = False
    
    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(computerword_ss_xy[0], (200,60))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(computerword_ss_xy[1], (200,60))
        else:
            self.unselect()
class TeacherWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Teacher'
        self.image = spritesheet.subsurface(teacherword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[8])
        self.selected = False

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(teacherword_ss_xy[0], (200,60))

    def change_ss(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(teacherword_ss_xy[1], (200,60))
        else:
            self.unselect()

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
def unselect_all_objects():
    car.unselect()
    apple.unselect()
    cellphone.unselect()
    house.unselect()
    classe.unselect()
    door.unselect()
    bike.unselect()
    computer.unselect()
    teacher.unselect()

# Palavras de Objetos
all_word_sprites = pygame.sprite.Group()
carw = CarWord()
applew = AppleWord()
cellphonew = CellphoneWord()
housew = HouseWord()
classew = ClasseWord()
doorw = DoorWord()
bikew = BikeWord()
computerw = ComputerWord()
teacherw = TeacherWord()
def unselect_all_words():
    carw.unselect()
    applew.unselect()
    cellphonew.unselect()
    housew.unselect()
    classew.unselect()
    doorw.unselect()
    bikew.unselect()
    computerw.unselect()
    teacherw.unselect()

# Lista que será usada para randomizar quais objetos aparecerá na tela
lista_img = [car, apple, cellphone, house, classe, door, bike, computer, teacher]
# Lista que será usada para randomizar quais palavras aparecerá na tela
lista_words = [carw, applew, cellphonew, housew, classew, doorw, bikew, computerw, teacherw]

word_index = []
img_index = []

while True:
    clock.tick(60)
    screen.fill((255, 255, 255))

    # Recebe a posição do mouse na tela
    mx, my = pygame.mouse.get_pos()
    loc = [mx, my]
    click = []
    cursor.cursor_pos(loc)

    # Recebe inputs de Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            click = loc
            click_area = pygame.draw.rect(screen, (0,0,0), (click[0], click[1], 10, 10))
            print(click)       
            
    # Armazena randomicamente um item da lista de palavras numa nova lista, que será utilizada para exibir as palavras na tela
    i_cont = []
    if random_list == True:
        random_list = False
        for w in range (0,4):
            i = randint(0, (len(lista_words)-1))
            i_cont.append(i)

            # Previne que o algoritmo gere índices repetidos ---------------------------------#
            while (i_cont.count(i) > 1):
                i_cont.pop()
                i = randint(0, (len(lista_words)-1))
                i_cont.append(i)

            random_words.append(lista_words[i])
            random_sprites.append(lista_img[i])
        # Insere no spriteGroup a lista de sprites randomiza, casando imagem com palavra
        all_object_sprites.add(random_sprites)
        all_word_sprites.add(random_words)

    # Exibe elementos(sprites) na tela -----------------------------------#

    all_object_sprites.draw(screen)
    all_word_sprites.draw(screen)
    cursor_sprite.draw(screen)
    
    # Recebem o estado das instancias 'selected' dos Objetos

    selected_object = [car.selected, apple.selected, cellphone.selected, house.selected, classe.selected, door.selected, bike.selected, computer.selected, teacher.selected]

    selected_word = [carw.selected, applew.selected, cellphonew.selected, housew.selected, classew.selected, doorw.selected, bikew.selected, computerw.selected, teacherw.selected]

    # Colisões e alteração de estado dos objetos(sprites) -----------------#

    if len(click) > 0:
        if click_area.colliderect(car.rect):
            if selected_object.count(True) <= 1:
                car.change_ss()

        elif click_area.colliderect(apple.rect):
            if selected_object.count(True) <= 1:
                apple.change_ss()

        elif click_area.colliderect(cellphone.rect):
            if selected_object.count(True) <= 1:
                cellphone.change_ss()

        elif click_area.colliderect(house.rect):
            if selected_object.count(True) <= 1:
                house.change_ss()

        elif click_area.colliderect(classe.rect):
            if selected_object.count(True) <= 1:
                classe.change_ss()

        elif click_area.colliderect(door.rect):
            if selected_object.count(True) <= 1:
                door.change_ss()

        elif click_area.colliderect(bike.rect):
            if selected_object.count(True) <= 1:
                bike.change_ss()

        elif click_area.colliderect(computer.rect):
            if selected_object.count(True) <= 1:
                computer.change_ss()

        elif click_area.colliderect(teacher.rect):
            if selected_object.count(True) <= 1:
                teacher.change_ss()

    # Colisões e alteração de estado das palavras ----------------------------#

        elif click_area.colliderect(car.rect):
            if selected_object.count(True) <= 1:
                car.change_ss()

        elif click_area.colliderect(apple.rect):
            if selected_object.count(True) <= 1:
                apple.change_ss()

        elif click_area.colliderect(cellphone.rect):
            if selected_object.count(True) <= 1:
                cellphone.change_ss()

        elif click_area.colliderect(house.rect):
            if selected_object.count(True) <= 1:
                house.change_ss()

        elif click_area.colliderect(classe.rect):
            if selected_object.count(True) <= 1:
                classe.change_ss()

        elif click_area.colliderect(door.rect):
            if selected_object.count(True) <= 1:
                door.change_ss()

        elif click_area.colliderect(bike.rect):
            if selected_object.count(True) <= 1:
                bike.change_ss()

        elif click_area.colliderect(computer.rect):
            if selected_object.count(True) <= 1:
                computer.change_ss()

        elif click_area.colliderect(teacher.rect):
            if selected_object.count(True) <= 1:
                teacher.change_ss()

    if selected_object.count(True) > 1:
        unselect_all_objects()
    
    pygame.display.flip()
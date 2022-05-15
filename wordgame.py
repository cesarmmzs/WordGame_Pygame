from asyncio import selector_events
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
word_pos = [(160, 60), (160, 125), (160, 190), (160, 255), (160, 320), (160,385), (160, 450), (160, 515), (160, 580)]
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
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet.subsurface(car_ss_xy[2], (100,100))

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(car_ss_xy[0], (100, 100))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet.subsurface(car_ss_xy[1], (100, 100))
            else:
                self.unselect()
        else:
            pass
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Apple'
        self.image = spritesheet.subsurface(apple_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[1])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet.subsurface(apple_ss_xy[2], (100,100))

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(apple_ss_xy[0], (100, 100))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet.subsurface(apple_ss_xy[1], (100, 100))
            else:
                self.unselect()
        else:
            pass
class Cellphone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Cellphone'
        self.image = spritesheet.subsurface(cellphone_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[2])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet.subsurface(cellphone_ss_xy[2], (100,100))

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(cellphone_ss_xy[0], (100, 100))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet.subsurface(cellphone_ss_xy[1], (100, 100))
            else:
                self.unselect()
        else:
            pass
class House(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'House'
        self.image = spritesheet.subsurface(house_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[3])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet.subsurface(house_ss_xy[2], (100,100))

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(house_ss_xy[0], (100, 100))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet.subsurface(house_ss_xy[1], (100, 100))
            else:
                self.unselect()
        else:
            pass
class Classe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Classe'
        self.image = spritesheet.subsurface(classe_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[4])
        self.selected = False
        self.success = False
    
    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet.subsurface(classe_ss_xy[2], (100,100))
    
    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(classe_ss_xy[0], (100, 100))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet.subsurface(classe_ss_xy[1], (100, 100))
            else:
                self.unselect()
        else:
            pass
class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Door'
        self.image = spritesheet.subsurface(door_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[5])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet.subsurface(door_ss_xy[2], (100,100))

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(door_ss_xy[0], (100, 100))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet.subsurface(door_ss_xy[1], (100, 100))
            else:
                self.unselect()
        else:
            pass
class Bike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Bike'
        self.image = spritesheet.subsurface(bike_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[6])
        self.selected = False
        self.success = False
    
    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet.subsurface(bike_ss_xy[2], (100,100))

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(bike_ss_xy[0], (100, 100))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet.subsurface(bike_ss_xy[1], (100, 100))
            else:
                self.unselect()
        else:
            pass
class Computer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Computer'
        self.image = spritesheet.subsurface(computer_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[7])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet.subsurface(computer_ss_xy[2], (100,100))

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(computer_ss_xy[0], (100, 100))

    def change_select(self):
        if self.selected == False:
            self.selected = True
            self.image = spritesheet.subsurface(computer_ss_xy[1], (100, 100))
        else:
            self.unselect()
class Teacher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Teacher'
        self.image = spritesheet.subsurface(teacher_ss_xy[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random_img_pos[8])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet.subsurface(teacher_ss_xy[2], (100,100))

    def unselect(self):
        self.selected = False
        self.image = spritesheet.subsurface(teacher_ss_xy[0], (100, 100))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet.subsurface(teacher_ss_xy[1], (100, 100))
            else:
                self.unselect()
        else:
            pass

# Sprites das Palavras (TERMINAR)
class CarWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Car'
        self.image = spritesheet2.subsurface(carword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[0])
        self.selected = False
        self.success = False
    
    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet2.subsurface(carword_ss_xy[2], (200,60))

    def unselect(self):
        self.selected = False
        self.image = spritesheet2.subsurface(carword_ss_xy[0], (200,60))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet2.subsurface(carword_ss_xy[1], (200,60))
            else:
                self.unselect()
        else:
            pass
class AppleWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Apple'
        self.image = spritesheet2.subsurface(appleword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[1])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet2.subsurface(appleword_ss_xy[2], (200,60))

    def unselect(self):
        self.selected = False
        self.image = spritesheet2.subsurface(appleword_ss_xy[0], (200,60))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet2.subsurface(appleword_ss_xy[1], (200,60))
            else:
                self.unselect()
        else:
            pass
class CellphoneWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Cellphone'
        self.image = spritesheet2.subsurface(cellphoneword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[2])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet2.subsurface(cellphoneword_ss_xy[2], (200,60))

    def unselect(self):
        self.selected = False
        self.image = spritesheet2.subsurface(cellphoneword_ss_xy[0], (200,60))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet2.subsurface(cellphoneword_ss_xy[1], (200,60))
            else:
                self.unselect()
        else:
            pass
class HouseWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'House'
        self.image = spritesheet2.subsurface(houseword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[3])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet2.subsurface(houseword_ss_xy[2], (200,60))

    def unselect(self):
        self.selected = False
        self.image = spritesheet2.subsurface(houseword_ss_xy[0], (200,60))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet2.subsurface(houseword_ss_xy[1], (200,60))
            else:
                self.unselect()
        else:
            pass
class ClasseWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Classe'
        self.image = spritesheet2.subsurface(classeword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[4])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet2.subsurface(classeword_ss_xy[2], (200,60))

    def unselect(self):
        self.selected = False
        self.image = spritesheet2.subsurface(classeword_ss_xy[0], (200,60))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet2.subsurface(classeword_ss_xy[1], (200,60))
            else:
                self.unselect()
        else:
            pass
class DoorWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Door'
        self.image = spritesheet2.subsurface(doorword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[5])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet2.subsurface(doorword_ss_xy[2], (200,60))

    def unselect(self):
        self.selected = False
        self.image = spritesheet2.subsurface(doorword_ss_xy[0], (200,60))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet2.subsurface(doorword_ss_xy[1], (200,60))
            else:
                self.unselect()
        else:
            pass
class BikeWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Bike'
        self.image = spritesheet2.subsurface(bikeword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[6])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet2.subsurface(bikeword_ss_xy[2], (200,60))

    def unselect(self):
        self.selected = False
        self.image = spritesheet2.subsurface(bikeword_ss_xy[0], (200,60))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet2.subsurface(bikeword_ss_xy[1], (200,60))
            else:
                self.unselect()
        else:
            pass
class ComputerWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Computer'
        self.image = spritesheet2.subsurface(computerword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[7])
        self.selected = False
        self.success = False
    
    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet2.subsurface(computerword_ss_xy[2], (200, 60))

    def unselect(self):
        self.selected = False
        self.image = spritesheet2.subsurface(computerword_ss_xy[0], (200,60))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet2.subsurface(computerword_ss_xy[1], (200,60))
            else:
                self.unselect()
        else:
            pass
class TeacherWord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Teacher'
        self.image = spritesheet2.subsurface(teacherword_ss_xy[0], (200,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random_word_pos[8])
        self.selected = False
        self.success = False

    def confirm_success(self):
        self.success = True
        self.selected = False
        self.image = spritesheet2.subsurface(teacherword_ss_xy[2], (200,60))

    def unselect(self):
        self.selected = False
        self.image = spritesheet2.subsurface(teacherword_ss_xy[0], (200,60))

    def change_select(self):
        if self.success == False:
            if self.selected == False:
                self.selected = True
                self.image = spritesheet2.subsurface(teacherword_ss_xy[1], (200,60))
            else:
                self.unselect()
        else:
            pass

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
select_match = []

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

    screen.blit(background, (0, 0))
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
                car.change_select()
                select_match.append(car.name)

        elif click_area.colliderect(apple.rect):
            if selected_object.count(True) <= 1:
                apple.change_select()
                select_match.append(apple.name)

        elif click_area.colliderect(cellphone.rect):
            if selected_object.count(True) <= 1:
                cellphone.change_select()
                select_match.append(cellphone.name)

        elif click_area.colliderect(house.rect):
            if selected_object.count(True) <= 1:
                house.change_select()
                select_match.append(house.name)

        elif click_area.colliderect(classe.rect):
            if selected_object.count(True) <= 1:
                classe.change_select()
                select_match.append(classe.name)

        elif click_area.colliderect(door.rect):
            if selected_object.count(True) <= 1:
                door.change_select()
                select_match.append(door.name)

        elif click_area.colliderect(bike.rect):
            if selected_object.count(True) <= 1:
                bike.change_select()
                select_match.append(bike.name)

        elif click_area.colliderect(computer.rect):
            if selected_object.count(True) <= 1:
                computer.change_select()
                select_match.append(computer.name)

        elif click_area.colliderect(teacher.rect):
            if selected_object.count(True) <= 1:
                teacher.change_select()
                select_match.append(teacher.name)

    # Colisões e alteração de estado das palavras ----------------------------#

        elif click_area.colliderect(carw.rect):
            if selected_word.count(True) <= 1:
                carw.change_select()
                select_match.append(carw.name)

        elif click_area.colliderect(applew.rect):
            if selected_word.count(True) <= 1:
                applew.change_select()
                select_match.append(applew.name)

        elif click_area.colliderect(cellphonew.rect):
            if selected_word.count(True) <= 1:
                cellphonew.change_select()
                select_match.append(cellphonew.name)

        elif click_area.colliderect(housew.rect):
            if selected_word.count(True) <= 1:
                housew.change_select()
                select_match.append(housew.name)

        elif click_area.colliderect(classew.rect):
            if selected_word.count(True) <= 1:
                classew.change_select()
                select_match.append(classew.name)

        elif click_area.colliderect(doorw.rect):
            if selected_word.count(True) <= 1:
                doorw.change_select()
                select_match.append(doorw.name)

        elif click_area.colliderect(bikew.rect):
            if selected_word.count(True) <= 1:
                bikew.change_select()
                select_match.append(bikew.name)

        elif click_area.colliderect(computerw.rect):
            if selected_word.count(True) <= 1:
                computerw.change_select()
                select_match.append(computerw.name)

        elif click_area.colliderect(teacherw.rect):
            if selected_word.count(True) <= 1:
                teacherw.change_select()
                select_match.append(teacherw.name)

    if len(select_match) == 2:
        if ((select_match[0] == 'Car') and (select_match[1] == 'Car')):
            car.confirm_success()
            carw.confirm_success()
            

        elif ((select_match[0] == 'Apple') and (select_match[1] == 'Apple')):
            apple.confirm_success()
            applew.confirm_success()
        
        elif ((select_match[0] == 'Cellphone') and (select_match[1] == 'Cellphone')):
            cellphone.confirm_success()
            cellphonew.confirm_success()

        elif ((select_match[0] == 'House') and (select_match[1] == 'House')):
            house.confirm_success()
            housew.confirm_success()

        elif ((select_match[0] == 'Class') and (select_match[1] == 'Class')):
            classe.confirm_success()
            classew.confirm_success()

        elif ((select_match[0] == 'Door') and (select_match[1] == 'Door')):
            door.confirm_success()
            doorw.confirm_success()

        elif ((select_match[0] == 'Bike') and (select_match[1] == 'Bike')):
            bike.confirm_success()
            bikew.confirm_success()

        elif ((select_match[0] == 'Computer') and (select_match[1] == 'Computer')):
            computer.confirm_success()
            computerw.confirm_success()
        
        elif ((select_match[0] == 'Teacher') and (select_match[1] == 'Teacher')):
            teacher.confirm_success()
            teacherw.confirm_success()

        select_match = []

    if selected_object.count(True) > 1:
        unselect_all_objects()
        unselect_all_words()

    if selected_word.count(True) > 1:
        unselect_all_words()
        unselect_all_objects()
    
    pygame.display.flip()
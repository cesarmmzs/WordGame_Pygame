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
w = 900
h = 675

# Algoritmo para randomizar a posição das palavras na tela (AUTO)
i_cont = []
word_pos = [(120, 60), (120, 125), (120, 190), (120, 255), (120, 320), (120,385), (120, 450), (120, 515), (120, 580)]
random_word_pos = []
for p in range (len(word_pos)):
    i = randint(0, len(word_pos)-1)
    i_cont.append(i)

    while (i_cont.count(i) > 1):
        i_cont.pop()
        i = randint(0, len(word_pos)-1)
        i_cont.append(i)
    random_word_pos.append(word_pos[i])

# Algoritmo para randomizar a posição das imagens na tela (AUTO)
i_cont = []
img_pos = [(350, 200), (350, 400), (350, 600), (570, 200), (570, 400), (570, 600), (800, 200), (800, 400), (800, 600)]
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

# Lista de Palavras
palavras = (
    ('Car', 'Apple', 'Cellphone', 'House', 'Class', 'Door', 'Bike', 'Computer', 'Teacher'),
    ('Earth','Target','Window','Crown','Whistle','Eyeliner','Cheese','Strawberry','Heaphone'),
    ('Schedule','Squirrel','Dessert','Olives','Scissor','Moisturizer','Hurricane','Workout','Eye Shadow')
    )
spritesheets = (('objectSpritesheet1.png','objectSpritesheet2.png','objectSpritesheet3.png'), ('wordSpritesheet1.png','wordSpritesheet2.png','wordSpritesheet3.png'),('menuSpritesheet.png'))

# Inicializando tela, plano de fundo e sprites que vão aparecer na tela
screen = pygame.display.set_mode((w,h))
menuspritesheet = pygame.image.load(os.path.join(img_dir, spritesheets[2])).convert_alpha()
arrowlist1 = ((0,200), (200,200))
arrowlist2 = ((100,200),(300,200))

# Nome da Página, Utilização do Clock para definir FrameRate
pygame.display.set_caption('Word Game - Aprendendo Inglês')
clock = pygame.time.Clock()
counter, textcounter = 60, '60'.rjust(2)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.Font(os.path.join(font_dir ,'rudiment.ttf'), 70)

# Listas  de posições das Imagens dentro da Spritesheet -> subsurface
object1_ss_xy = [(0,0), (0, 100), (0, 200)]
object2_ss_xy = [(100, 0), (100, 100), (100, 200)]
object3_ss_xy = [(200, 0), (200, 100), (200, 200)]
object4_ss_xy = [(300, 0), (300, 100), (300, 200)]
object5_ss_xy = [(400, 0), (400, 100), (400, 200)]
object6_ss_xy = [(500, 0), (500, 100), (500, 200)]
object7_ss_xy = [(600, 0), (600, 100), (600, 200)]
object8_ss_xy = [(700, 0), (700, 100), (700, 200)]
object9_ss_xy = [(800, 0), (800, 100), (800, 200)]

# Listas  de posições das Palavras dentro da Spritesheet -> subsurface
word1_ss_xy = [(0,0), (200, 0), (400, 0)]
word2_ss_xy = [(0, 60), (200, 60), (400, 60)]
word3_ss_xy = [(0, 120), (200, 120), (400, 120)]
word4_ss_xy = [(0, 180), (200, 180), (400, 180)]
word5_ss_xy = [(0, 240), (200, 240), (400, 240)]
word6_ss_xy = [(0, 300), (200, 300), (400, 300)]
word7_ss_xy = [(0, 360), (200, 360), (400, 360)]
word8_ss_xy = [(0, 420), (200, 420), (400, 420)]
word9_xx_xy = [(0, 480), (200, 480), (400, 480)]

# Variável que será utilizada para determinar que as spritesheets só serão randomizadas uma vez
random_list = True

#Sprites dos Menus
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

# Instanciando Objetos de Sprites

# Menu
all_menu_sprites = pygame.sprite.Group()
initgame = Init()
difficult = Difficult()
difficult_set = DifficultSet()
arrow1 = Arrow1()
arrow2 = Arrow2()
all_menu_sprites.add(initgame, difficult, difficult_set, arrow1, arrow2)

# INÍCIO DO JOGO
while True:

    # ------------- MENU -------------------
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

    #if difficult_set.difficult == 0:

        # Sprites dos Objetos
    class Object1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[0]
            self.image = spritesheet.subsurface(object1_ss_xy[0], (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (random_img_pos[0])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet.subsurface(object1_ss_xy[2], (100,100))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet.subsurface(object1_ss_xy[0], (100, 100))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet.subsurface(object1_ss_xy[1], (100, 100))
                else:
                    self.unselect()
            else:
                pass
    class Object2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[1]
            self.image = spritesheet.subsurface(object2_ss_xy[0], (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (random_img_pos[1])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet.subsurface(object2_ss_xy[2], (100,100))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.image = spritesheet.subsurface(object2_ss_xy[0], (100, 100))
                self.selected = False

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet.subsurface(object2_ss_xy[1], (100, 100))
                else:
                    self.unselect()
            else:
                pass
    class Object3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[2]
            self.image = spritesheet.subsurface(object3_ss_xy[0], (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (random_img_pos[2])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet.subsurface(object3_ss_xy[2], (100,100))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet.subsurface(object3_ss_xy[0], (100, 100))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet.subsurface(object3_ss_xy[1], (100, 100))
                else:
                    self.unselect()
            else:
                pass
    class Object4(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[3]
            self.image = spritesheet.subsurface(object4_ss_xy[0], (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (random_img_pos[3])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet.subsurface(object4_ss_xy[2], (100,100))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet.subsurface(object4_ss_xy[0], (100, 100))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet.subsurface(object4_ss_xy[1], (100, 100))
                else:
                    self.unselect()
            else:
                pass
    class Object5(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[4]
            self.image = spritesheet.subsurface(object5_ss_xy[0], (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (random_img_pos[4])
            self.selected = False
            self.success = False
        
        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet.subsurface(object5_ss_xy[2], (100,100))
        
        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet.subsurface(object5_ss_xy[0], (100, 100))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet.subsurface(object5_ss_xy[1], (100, 100))
                else:
                    self.unselect()
            else:
                pass
    class Object6(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[5]
            self.image = spritesheet.subsurface(object6_ss_xy[0], (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (random_img_pos[5])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet.subsurface(object6_ss_xy[2], (100,100))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet.subsurface(object6_ss_xy[0], (100, 100))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet.subsurface(object6_ss_xy[1], (100, 100))
                else:
                    self.unselect()
            else:
                pass
    class Object7(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[6]
            self.image = spritesheet.subsurface(object7_ss_xy[0], (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (random_img_pos[6])
            self.selected = False
            self.success = False
        
        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet.subsurface(object7_ss_xy[2], (100,100))

        def unselect(self):
            self.selected = False
            self.image = spritesheet.subsurface(object7_ss_xy[0], (100, 100))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet.subsurface(object7_ss_xy[1], (100, 100))
                else:
                    self.unselect()
            else:
                pass
    class Object8(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[7]
            self.image = spritesheet.subsurface(object8_ss_xy[0], (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (random_img_pos[7])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet.subsurface(object8_ss_xy[2], (100,100))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet.subsurface(object8_ss_xy[0], (100, 100))

        def change_select(self):
            if self.selected == False:
                self.selected = True
                self.image = spritesheet.subsurface(object8_ss_xy[1], (100, 100))
            else:
                self.unselect()
    class Object9(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[8]
            self.image = spritesheet.subsurface(object9_ss_xy[0], (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (random_img_pos[8])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet.subsurface(object9_ss_xy[2], (100,100))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet.subsurface(object9_ss_xy[0], (100, 100))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet.subsurface(object9_ss_xy[1], (100, 100))
                else:
                    self.unselect()
            else:
                pass

    # Sprites das Palavras
    class Object1Word(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[0]
            self.image = spritesheet2.subsurface(word1_ss_xy[0], (200,60))
            self.rect = self.image.get_rect()
            self.rect.center = (random_word_pos[0])
            self.selected = False
            self.success = False
        
        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet2.subsurface(word1_ss_xy[2], (200,60))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet2.subsurface(word1_ss_xy[0], (200,60))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet2.subsurface(word1_ss_xy[1], (200,60))
                else:
                    self.unselect()
            else:
                pass
    class Object2Word(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[1]
            self.image = spritesheet2.subsurface(word2_ss_xy[0], (200,60))
            self.rect = self.image.get_rect()
            self.rect.center = (random_word_pos[1])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet2.subsurface(word2_ss_xy[2], (200,60))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet2.subsurface(word2_ss_xy[0], (200,60))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet2.subsurface(word2_ss_xy[1], (200,60))
                else:
                    self.unselect()
            else:
                pass
    class Object3Word(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[2]
            self.image = spritesheet2.subsurface(word3_ss_xy[0], (200,60))
            self.rect = self.image.get_rect()
            self.rect.center = (random_word_pos[2])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet2.subsurface(word3_ss_xy[2], (200,60))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet2.subsurface(word3_ss_xy[0], (200,60))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet2.subsurface(word3_ss_xy[1], (200,60))
                else:
                    self.unselect()
            else:
                pass
    class Object4Word(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[3]
            self.image = spritesheet2.subsurface(word4_ss_xy[0], (200,60))
            self.rect = self.image.get_rect()
            self.rect.center = (random_word_pos[3])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet2.subsurface(word4_ss_xy[2], (200,60))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet2.subsurface(word4_ss_xy[0], (200,60))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet2.subsurface(word4_ss_xy[1], (200,60))
                else:
                    self.unselect()
            else:
                pass
    class Object5Word(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = 'Class'
            self.image = spritesheet2.subsurface(word5_ss_xy[0], (200,60))
            self.rect = self.image.get_rect()
            self.rect.center = (random_word_pos[4])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet2.subsurface(word5_ss_xy[2], (200,60))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet2.subsurface(word5_ss_xy[0], (200,60))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet2.subsurface(word5_ss_xy[1], (200,60))
                else:
                    self.unselect()
            else:
                pass
    class Object6Word(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[5]
            self.image = spritesheet2.subsurface(word6_ss_xy[0], (200,60))
            self.rect = self.image.get_rect()
            self.rect.center = (random_word_pos[5])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet2.subsurface(word6_ss_xy[2], (200,60))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet2.subsurface(word6_ss_xy[0], (200,60))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet2.subsurface(word6_ss_xy[1], (200,60))
                else:
                    self.unselect()
            else:
                pass
    class Object7Word(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[6]
            self.image = spritesheet2.subsurface(word7_ss_xy[0], (200,60))
            self.rect = self.image.get_rect()
            self.rect.center = (random_word_pos[6])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet2.subsurface(word7_ss_xy[2], (200,60))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet2.subsurface(word7_ss_xy[0], (200,60))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet2.subsurface(word7_ss_xy[1], (200,60))
                else:
                    self.unselect()
            else:
                pass
    class Object8Word(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[7]
            self.image = spritesheet2.subsurface(word8_ss_xy[0], (200,60))
            self.rect = self.image.get_rect()
            self.rect.center = (random_word_pos[7])
            self.selected = False
            self.success = False
        
        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet2.subsurface(word8_ss_xy[2], (200, 60))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet2.subsurface(word8_ss_xy[0], (200,60))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet2.subsurface(word8_ss_xy[1], (200,60))
                else:
                    self.unselect()
            else:
                pass
    class Object9Word(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.name = palavras_selecionadas[8]
            self.image = spritesheet2.subsurface(word9_xx_xy[0], (200,60))
            self.rect = self.image.get_rect()
            self.rect.center = (random_word_pos[8])
            self.selected = False
            self.success = False

        def confirm_success(self):
            self.success = True
            self.selected = False
            self.image = spritesheet2.subsurface(word9_xx_xy[2], (200,60))

        def unselect(self):
            if self.success == True:
                pass
            else:
                self.selected = False
                self.image = spritesheet2.subsurface(word9_xx_xy[0], (200,60))

        def change_select(self):
            if self.success == False:
                if self.selected == False:
                    self.selected = True
                    self.image = spritesheet2.subsurface(word9_xx_xy[1], (200,60))
                else:
                    self.unselect()
            else:
                pass

    # Instanciando Objectos de Sprites

    # Imagens
    all_object_sprites = pygame.sprite.Group()
    object1 = Object1()
    object2 = Object2()
    object3 = Object3()
    object4 = Object4()
    object5 = Object5()
    object6 = Object6()
    object7 = Object7()
    object8 = Object8()
    object9 = Object9()

    def unselect_all_objects():
        object1.unselect()
        object2.unselect()
        object3.unselect()
        object4.unselect()
        object5.unselect()
        object6.unselect()
        object7.unselect()
        object8.unselect()
        object9.unselect()

    # Palavras
    all_word_sprites = pygame.sprite.Group()
    object1word = Object1Word()
    object2word = Object2Word()
    object3word = Object3Word()
    object4word = Object4Word()
    object5word = Object5Word()
    object6word = Object6Word()
    object7word = Object7Word()
    object8word = Object8Word()
    object9word = Object9Word()

    def unselect_all_words():
        object1word.unselect()
        object2word.unselect()
        object3word.unselect()
        object4word.unselect()
        object5word.unselect()
        object6word.unselect()
        object7word.unselect()
        object8word.unselect()
        object9word.unselect()

    # Lista que será usada para randomizar quais objetos aparecerá na tela
    lista_img = [object1, object2, object3, object4, object5, object6, object7, object8, object9]
    # Lista que será usada para randomizar quais palavras aparecerá na tela
    lista_palavras = [object1word, object2word, object3word, object4word, object5word, object6word, object7word, object8word, object9word]

    word_index = []
    img_index = []
    select_match = []

    background = pygame.image.load(os.path.join(img_dir, 'wordgame_bg.jpg')).convert()
    spritesheet = pygame.image.load(os.path.join(img_dir, spritesheets[0][indice_objetos_selecionados])).convert_alpha()
    spritesheet2 = pygame.image.load(os.path.join(img_dir, spritesheets[1][0])).convert_alpha()
    palavras_selecionadas = palavras[indice_palavras_selecionadas]

    # -------------------- JOGO --------------------
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
            if event.type == pygame.USEREVENT:
                counter -= 1
                textcounter = str(counter).rjust(2) if counter > 0 else 'Fim de Jogo!'

        # Armazena randomicamente um item da lista de palavras numa nova lista, que será utilizada para exibir as palavras na tela
        i_cont = []
        if random_list == True:
            random_list = False
            for w in range (0, onscreen_objects):
                i = randint(0, (len(palavras)-1))
                i_cont.append(i)

                # Previne que o algoritmo gere índices repetidos ---------------------------------#
                while (i_cont.count(i) > 1):
                    i_cont.pop()
                    i = randint(0, (len(palavras)-1))
                    i_cont.append(i)

                random_words.append(palavras[i])
                random_sprites.append(lista_img[i])
            # Insere no spriteGroup a lista de sprites randomiza, casando imagem com palavra
            all_object_sprites.add(random_sprites)
            all_word_sprites.add(random_words)

        # Exibe elementos(sprites) na tela -----------------------------------#

        screen.blit(background, (0, 0))
        all_object_sprites.draw(screen)
        all_word_sprites.draw(screen)
        
        # Recebem o estado das instancias 'selected' dos Objetos

        selected_object = [object1.selected, object2.selected, object3.selected, object4.selected, object5.selected, object6.selected, object7.selected, object8.selected, object9.selected]

        selected_word = [object1word.selected, object2word.selected, object3word.selected, object4word.selected, object5word.selected, object6word.selected, object7word.selected, object8word.selected, object9word.selected]

        # Colisões e alteração de estado dos objetos(sprites) -----------------#

        if len(click) > 0:

            if click_area.colliderect(object1.rect):
                if object1.selected == True:
                    pass
                elif selected_object.count(True) <= 1:
                    object1.change_select()
                    select_match.append(object1.name)

            elif click_area.colliderect(object2.rect):
                if object2.selected == True:
                    pass
                elif selected_object.count(True) <= 1:
                    object2.change_select()
                    select_match.append(object2.name)

            elif click_area.colliderect(object3.rect):
                if object3.selected == True:
                    pass
                elif selected_object.count(True) <= 1:
                    object3.change_select()
                    select_match.append(object3.name)

            elif click_area.colliderect(object4.rect):
                if object4.selected == True:
                    pass
                elif selected_object.count(True) <= 1:
                    object4.change_select()
                    select_match.append(object4.name)

            elif click_area.colliderect(object5.rect):
                if object5.selected == True:
                    pass
                elif selected_object.count(True) <= 1:
                    object5.change_select()
                    select_match.append(object5.name)

            elif click_area.colliderect(object6.rect):
                if object6.selected == True:
                    pass
                elif selected_object.count(True) <= 1:
                    object6.change_select()
                    select_match.append(object6.name)

            elif click_area.colliderect(object7.rect):
                if object7.selected == True:
                    pass
                elif selected_object.count(True) <= 1:
                    object7.change_select()
                    select_match.append(object7.name)

            elif click_area.colliderect(object8.rect):
                if object8.selected == True:
                    pass
                elif selected_object.count(True) <= 1:
                    object8.change_select()
                    select_match.append(object8.name)

            elif click_area.colliderect(object9.rect):
                if object9.selected == True:
                    pass
                elif selected_object.count(True) <= 1:
                    object9.change_select()
                    select_match.append(object9.name)

        # Colisões e alteração de estado das palavras ----------------------------#

            elif click_area.colliderect(object1word.rect):
                if object1word.selected == True:
                    pass
                elif selected_word.count(True) <= 1:
                    object1word.change_select()
                    select_match.append(object1word.name)

            elif click_area.colliderect(object2word.rect):
                if object2word.selected == True:
                    pass
                elif selected_word.count(True) <= 1:
                    object2word.change_select()
                    select_match.append(object2word.name)

            elif click_area.colliderect(object3word.rect):
                if object3word.selected == True:
                    pass
                elif selected_word.count(True) <= 1:
                    object3word.change_select()
                    select_match.append(object3word.name)

            elif click_area.colliderect(object4word.rect):
                if object4word.selected == True:
                    pass
                elif selected_word.count(True) <= 1:
                    object4word.change_select()
                    select_match.append(object4word.name)

            elif click_area.colliderect(object5word.rect):
                if object5word.selected == True:
                    pass
                elif selected_word.count(True) <= 1:
                    object5word.change_select()
                    select_match.append(object5word.name)

            elif click_area.colliderect(object6word.rect):
                if object6word.selected == True:
                    pass
                elif selected_word.count(True) <= 1:
                    object6word.change_select()
                    select_match.append(object6word.name)

            elif click_area.colliderect(object7word.rect):
                if object7word.selected == True:
                    pass
                elif selected_word.count(True) <= 1:
                    object7word.change_select()
                    select_match.append(object7word.name)

            elif click_area.colliderect(object8word.rect):
                if object8word.selected == True:
                    pass
                elif selected_word.count(True) <= 1:
                    object8word.change_select()
                    select_match.append(object8word.name)

            elif click_area.colliderect(object9word.rect):
                if object9word.selected == True:
                    pass
                elif selected_word.count(True) <= 1:
                    object9word.change_select()
                    select_match.append(object9word.name)
            
        if len(select_match) == 2:
            if ((select_match[0] == palavras_selecionadas[0]) and (select_match[1] == palavras_selecionadas[0])):
                object1.confirm_success()
                object1word.confirm_success()
                

            elif ((select_match[0] == palavras_selecionadas[1]) and (select_match[1] == palavras_selecionadas[1])):
                object2.confirm_success()
                object2word.confirm_success()
            
            elif ((select_match[0] == palavras_selecionadas[2]) and (select_match[1] == palavras_selecionadas[2])):
                object3.confirm_success()
                object3word.confirm_success()

            elif ((select_match[0] == palavras_selecionadas[3]) and (select_match[1] == palavras_selecionadas[4])):
                object4.confirm_success()
                object4word.confirm_success()

            elif ((select_match[0] == palavras_selecionadas[4]) and (select_match[1] == palavras_selecionadas[4])):
                object5.confirm_success()
                object5word.confirm_success()

            elif ((select_match[0] == palavras_selecionadas[5]) and (select_match[1] == palavras_selecionadas[5])):
                object6.confirm_success()
                object6word.confirm_success()

            elif ((select_match[0] == palavras_selecionadas[6]) and (select_match[1] == palavras_selecionadas[6])):
                object7.confirm_success()
                object7word.confirm_success()

            elif ((select_match[0] == palavras_selecionadas[7]) and (select_match[1] == palavras_selecionadas[7])):
                object8.confirm_success()
                object8word.confirm_success()
            
            elif ((select_match[0] == palavras_selecionadas[8]) and (select_match[1] == palavras_selecionadas[8])):
                object9.confirm_success()
                object9word.confirm_success()

            else:
                unselect_all_objects()
                unselect_all_words()

            select_match = []
        screen.blit(font.render(textcounter, True, (255, 255, 255)), (550, 30))
        pygame.display.flip()
        clock.tick(60)
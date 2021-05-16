from pygame import *
from random import randint
from time import time as timer

#Класс спрайта
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.speed_x = player_speed
        self.speed_y = int(player_speed/2)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#Класс игрока
class Player1(GameSprite):
    def update(self):
        global frame
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys_pressed[K_s] and self.rect.y< 595:
            self.rect.y += 5

class Player2(GameSprite):
    def update(self):
        global frame
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if keys_pressed[K_DOWN] and self.rect.y< 595:
            self.rect.y += 5

class Ball(GameSprite):
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y<1 or self.rect.y>549:
            self.speed_y*=-1
        if sprite.collide_rect(ball, p1) or sprite.collide_rect(ball, p2):
            self.speed_x*=-1
            
#Окно игры
window = display.set_mode((800,600))
display.set_caption('Cool Game')
#Фон сцены
bg = transform.scale(image.load('bg.jpg'), (800,600))

#Переменные
pong_sound ="pong.ogg"
clock = time.Clock()
FPS = 74
font.init()
lose = font.SysFont('Areal', 76).render('Поражение', True, (255, 255, 255))
win =  font.SysFont('Areal', 76).render('Победа', True, (255, 255, 255))
run = True
finish = False
racket_image = 'rаcket.png'
ball = "ball.png"
#Объекты
p1 = Player1(racket_image, 10, 100, 10, 250, 5)
p2 = Player2(racket_image, 10, 100, 780, 250, 5)
ball = Ball(ball, 50, 50, 250, 275, 5)


mixer.init()
pong = mixer.Sound('pong.ogg')


while run:
#Завершение игры
    for e in event.get():
        if e.type == QUIT:
            run = False


    if not(finish):
        window.blit(bg, (0,0))
        p1.update()
        p1.reset()
        p2.update()
        p2.reset()
        ball.update()
        ball.reset()
    display.update()
    clock.tick(FPS)
    new_time = timer()



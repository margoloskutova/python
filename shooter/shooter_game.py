from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption("Shooter Game")
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx,self.rect.top,15,30,15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        global lost

        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(30, 620)

            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

        if self.rect.y <= 0:
            self.kill()


lost = 0
score = 0

font.init()
font_lose = font.SySFont('Arial', 36)
font_win = font.SySFont('Arial', 36)

bullets = sprite.Group()
player = Player('rocket.png',300,430,65,75,5)
monsters = sprite.Group()

for i in range(5):
    enemy = Enemy('ufo.png', randint(30, 620), 0,90,50, randint(1, 3))
    monsters.add(enemy)

asteroid = Enemy('asteroid.png', randint(30,620), 0,90,50, 1)
monsters.add(asteroid)

for i in range(2):
    asteroid = Enemy('asteroid.png', randint(30,60), 0,90,50, 1 )
    monsters.add(asteroid)

mixer.init()
mixer.music.load('space.ogg')
fire_sound = mixer.Sound('fire.ogg')
mixer.music.play()

FPS = 60
clock = time.Clock()

font_over = font.SySFont('Arial', 56)
win_text = font_over.render('YOU WIN', True, (255, 255, 255))
lose_text = font_over.render('YOU LOSE', True, (255, 255, 255))
finish = False
game = True

while game:
    lost_score = font_lose.render('Пропущено: ' + str(lost), True, (255, 255, 255))
    win_score = font_win.render('Побеждено: ' + str(score), True, (255, 255, 255))

    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire()

    if finish != True:
        window.blit(background, (0, 0))
        
        monsters.update()
        player.update()
        bullets.update()

        window.blit(lost_score, (5, 70))
        window.blit(win_score, (5, 35))

        sprites_list = sprite.groupcollide(monsters,bullets,True,True)
        for i in sprites_list:
            score +=1
            enemy = Enemy('ufo.png',randint(30,620),0,90,50,randint(1,3))
            monsters.add(enemy)

        if score >= 10:
            finish = True
            window.blit(win_text,(250,200))


        if lost >= 3:
            finish = True
            window.blit(lose_text,(250,200))    


        monsters.draw(window)
        bullets.draw(window)
        player.reset()
        

    display.update()
    clock.tick(FPS)
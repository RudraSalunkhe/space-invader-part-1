import math
import random
import pygame

screen_width=500
screen_height=500
player_start_x=380
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=27

pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))

background_image=pygame.image.load("background.png")

pygame.display.set_caption("space invader")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerimg=pygame.image.load("player.png")
playerx=player_start_x
playery=player_start_y
playerx_change=0

enemyImg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemy=6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,screen_width-64))

    enemyy.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)

bulletImg=pygame.image.load("bullet.png")
bulletx=0
bullety=player_start_y
bulletx_change=0
bullety_change=bullet_speed_y
bullet_state="ready"

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=0
texty=0

over_font=pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score=font.render('score :'+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text=over_font.render('GAME OVER',True,(255,255,255))
    screen.blit(over_text(200,250))

def player(x,y):
    screen.blit(playerimg(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="free"
    screen.blit(bulletImg,(x+16,y+10))

def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((enemyx-enemyy)**2,(enemyy-bullety)**2)
    return distance<collision_distance

running=True
while  running:
    screen.fill(0,0,0)
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playery_change=-5
            if event.key==pygame.K_RIGHT:
                playerx_change=5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bulletx=playerx
            fire_bullet(bulletx,bullety)
        if event.type==pygame.KEYUP and event.key in (pygame.K_LEFT,pygame.K_RIGHT):
            playerx_change=0

            playerx=









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
bullet_speed=10
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

enemeys=[]
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


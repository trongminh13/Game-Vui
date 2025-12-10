import pygame
import os
import random
#Intialize the pygame

pygame.init()
screen = pygame.display.set_mode((1900, 1000))

pygame.display.set_caption("Space Invaders")
current_path = os.path.dirname(__file__)
image_ufo_path = os.path.join(current_path, "images/ufo/ufo.png")
image_space_path = os.path.join(current_path, "images/space-ship/spaceship.png")
image_enemy_path = os.path.join(current_path, "images/enemy/quang-hot.png")
image_background_path = os.path.join(current_path, "images/background/universe.jpg")
icon = pygame.image.load(image_ufo_path)
pygame.display.set_icon(icon)


background = pygame.image.load(image_background_path)
#player 
playerImg = pygame.image.load(image_space_path)
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 900
playerY = 800
playerX_change = 0

#enemy
enemyImg = pygame.image.load(image_enemy_path)
enemyImg = pygame.transform.scale(enemyImg, (90, 90))
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.5
enemyY_change = 40


def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

#game loop
running = True
while running:
       #RGB - Red, greem. blue 
    screen.fill((0,0,0))
    #backgound image
    screen.blit(background,(0,0))
    # playerY -= 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            #if keastroke is pressed check whether its right or left

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            playerX_change = -1
          if event.key == pygame.K_RIGHT:
            playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0

# 5 = 5 + -0.1 -> 5 = 5 - 0.1
# 5 = 5 + 0.1

    playerX += playerX_change

    if playerX <= 0:
       playerX = 0
    elif playerX >= 1837:
       playerX = 1837

#enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
       enemyX_change = 0.5
       enemyY += enemyY_change
    elif enemyX >= 1820:
       enemyX_change  = -0.5
       enemyY += enemyY_change

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
 
import pygame
import os
import math
import random
#Intialize the pygame
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((1900, 1000))

pygame.display.set_caption("Space Invaders")
current_path = os.path.dirname(__file__)
image_ufo_path = os.path.join(current_path, "images/ufo/ufo.png")
image_space_path = os.path.join(current_path, "images/space-ship/spaceship.png")
image_enemy_path = os.path.join(current_path, "images/enemy/quang-hot.png")
image_bullet_path = os.path.join(current_path, "images/weapons/bullet-yellow.png")
image_background_path = os.path.join(current_path, "images/background/universe.jpg")
bullet_Sound = mixer.Sound(os.path.join(current_path, "sounds/shot.wav"))
explosion_Sound = mixer.Sound(os.path.join(current_path, "sounds/explosion.wav"))
icon = pygame.image.load(image_ufo_path)
pygame.display.set_icon(icon)


background = pygame.image.load(image_background_path)

mixer.music.load("spaceInvader/sounds/background_sound.mp3")
mixer.music.play(-1)
#player 
playerImg = pygame.image.load(image_space_path)
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 900
playerY = 800
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    image = pygame.image.load(image_enemy_path)
    scaled_image = pygame.transform.scale(image, (100, 100))
    enemyImg.append(scaled_image)
    # enemyImg.append(pygame.image.load(image_enemy_path))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(3)
    enemyY_change.append(40)


#bullet

bulletImg = pygame.image.load(image_bullet_path)
bulletImg = pygame.transform.scale(bulletImg, (50, 50))
bulletX =0
bulletY = 700
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" #ready - you can't see the bullet on the screen and Fire - the bullet is currently moving
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
testY = 10

over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Da giet " + str(score_value) + " thang quang hot", True,(255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance <27:
        return True
    else:
        return False


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
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound.play()
                    #get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
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
    for i in range(num_of_enemies):

        if enemyY[i] > 600:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1820:
            enemyX_change[i]  = -3
        # enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i],bulletX,bulletY)
        if collision:
            explosion_Sound.play()
            bulletY = 700
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)
        
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 700
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change


    player(playerX,playerY)
    show_score(textX,testY)
    # enemy(enemyX, enemyY)
    pygame.display.update()

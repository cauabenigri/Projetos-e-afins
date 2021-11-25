import pygame
from random import randint

pygame.init()
running = True

screen = pygame.display.set_mode((800, 600))

# player

playerImg = pygame.image.load('img/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy
meteoroImg = []
meteoroX = []
meteoroY = []
meteoroX_change = []
meteoroY_change = []
for i in range(0, 5):
    meteoroImg.append(pygame.image.load('img/meteoro.png'))
    meteoroX.append(randint(0, 736))
    meteoroY.append(0)
    meteoroX_change.append(0)
    meteoroY_change.append(0.1)

def meteoro(x, y):
    screen.blit(meteoroImg[a], (x, y))


# events

while running:
    screen.fill((0, 0, 0))
    player(playerX, playerY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1
        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0
    if playerX <= 0:
        playerX = 0
    if playerX >= 768:
        playerX = 768
    if playerY <= 0:
        playerY = 0
    if playerY >= 568:
        playerY = 568

    for a in range(0, 5):
        meteoro(meteoroX[a], meteoroY[a])
        meteoroY[a] += meteoroY_change[a]

    if meteoroY[0] > 600:
        meteoroY.clear()
        meteoroY.append(0)

    playerX += playerX_change
    playerY += playerY_change
    pygame.display.update()

import pygame
import sys

pygame.init()

scale = 50


SCREENWIDTH = 1800
SCREENHEIGHT = 1000
GRIDSIZE = 40
FPS = 60
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), vsync=1)


playerImg = pygame.image.load("images/player.png").convert_alpha()
playerScaled = pygame.transform.scale(playerImg, (scale * 1, scale * 2))


offsetX = SCREENWIDTH/2 - playerScaled.width/2
offsetY = SCREENHEIGHT/2 - playerScaled.height/2
pygame.display.set_caption("My Pygame Window")
clock = pygame.time.Clock()
spriteImages = [pygame.image.load("images/smelter.png").convert_alpha(),
           pygame.image.load("images/InserterBase.png").convert_alpha()]

def run(sprites, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #logic
    wasd = [0,0,0,0]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        wasd[0] = 1
    if keys[pygame.K_a]:
        wasd[1] = 1
    if keys[pygame.K_s]:
        wasd[2] = 1
    if keys[pygame.K_d]:
        wasd[3] = 1

    screen.fill((158, 107, 58))   
    
    #drawing
    for i in sprites:
        if screen.get_rect().collidepoint((i.coords[0] * scale - player.coords[0] + offsetX + 50, i.coords[1] * scale - player.coords[1] + offsetY + 50)):
            scaled = pygame.transform.scale(spriteImages[i.data.type], (scale * i.data.width, scale * i.data.height))
            screen.blit(scaled, (i.coords[0] * scale - player.coords[0] + offsetX, i.coords[1] * scale - player.coords[1] + offsetY))

    screen.blit(playerScaled, (offsetX, offsetY))

    pygame.display.flip()

    clock.tick(FPS)
    return wasd
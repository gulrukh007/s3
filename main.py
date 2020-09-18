import pygame

#Initialize the pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 600))

#title and Icon
pygame.display.set_caption("Space Invader")

#player
playerimage = pygame.image.load('star.png')
playerX = 370
playerY = 80


def player():
    screen.blit(playerimage,(playerX,playerY))

#Game Loop
running = True
while running:
    # RGB red green blue
    screen.fill((255, 0, 0))
    playerX += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()



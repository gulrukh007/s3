import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# title and Icon
pygame.display.set_caption("Space Invader")

# player
playerimage = pygame.image.load('star.png')
playerX = 350
playerY = 450
playerX_change = 0

# ghost
ghostimage = pygame.image.load('ghost.png')
ghostX = random.randint(100,700)
ghostY = random.randint(50, 150)
ghostY_change = 0.3
ghostX_change = 50

# bullet
#ready = you cant see the bullet but the bullet is there
#Fire = when bullet is moving

bulletimage = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bulletX_change = 40
bullet_state = "ready"



#background
background = pygame.image.load('gg.jpg')

def player(x, y):
    screen.blit(playerimage, (x, y))


def ghost(x, y):
    screen.blit(ghostimage, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimage, (x + 16, y + 10))


# Game Loop
running = True
while running:
    # RGB red green blue
    screen.fill((255, 0, 0))

    #background Image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check weather it has to go left or right
        # keydown is pressing anykey
        if event.type == pygame.KEYDOWN:

            # k_left is going left
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            # k_right is going right
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            #space bullet
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX ,bulletY)


        # keyup is when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 700:
        playerX = 700

    # Enemy Movement
    ghostX += ghostX_change
    if ghostX <= 0:
        ghostX_change = 4
        ghostY += ghostX_change
    elif ghostX >= 700:
        ghostX_change = -0.3
        ghostY += ghostX_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change





    player(playerX, playerY)
    pygame.display.update()



    ghost(ghostX, ghostY)
    pygame.display.update()

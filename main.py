import pygame, sys, random, time

# check for initializing error
check_errors = pygame.init()
if check_errors[1] > 0:
    print(f"(!) Had {check_errors[1]} initializing errors, exiting ...")
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake game!")


# Colors
red = pygame.Color(255, 0, 0) # game over
green = pygame.Color(0, 255, 0) # snake
black = pygame.Color(0, 0, 0) # score
white = pygame.Color(255, 255, 255) # background
brown = pygame.Color(165, 42, 42) # food

# FPS controller
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 70)*10, random.randrange(1, 46)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    pygame.display.flip()

gameOver()
time.sleep(10)

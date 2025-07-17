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

foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
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
    time.sleep(4)
    pygame.quit() # pygame exit
    sys.exit() # console exit

# Main Logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'): # ASCII foe the key
                changeTo = 'LEFT'
            if event.key == pygame.K_DOWN or event.key == ord('s'): # ASCII foe the key
                changeTo = 'DOWN'
            if event.key == pygame.K_RIGHT or event.key == ord('l'): # ASCII foe the key
                changeTo = 'RIGHT'
            if event.key == pygame.K_UP or event.key == ord('w'): # ASCII foe the key
                changeTo = 'UP'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                # pygame.event.post(pygame.event.Event(QUIT))

    # Validation of direction
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Update snake position [x, y]
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # Snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
    else:
        snakeBody.pop()

    # Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
    foodSpawn = True
import pygame
from sys import exit

# this is bascially the indicating the start of the car 
# imagine this as starting the car using the key, the engine fires up
# for us in short it means that now we can use pygames ...
pygame.init()

# setting up the display screen for it to display our game 
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
screen.fill('White')

# adding a title for the game, screen ...
pygame.display.set_caption('Runner')

# creating a clock, for the framerates and other niche things
clock = pygame.time.Clock()

# creating a font 
test_font = pygame.font.Font('Fonts/Font.ttf', 20)

# creating surface for the images 
    # .convert_alpha() converts the images into a more workable format for the pygame
    # in theory making our game more optimized ... 
background_surface = pygame.image.load('Images/background.png').convert_alpha()
ground_surface = pygame.image.load('Images/GroundImage.png').convert_alpha()
cloud_surface = pygame.image.load('Images/Clouds.png').convert_alpha()

cactus_surface = pygame.image.load('Images/Cactus/Cactus2.png').convert_alpha()
cactus_rectangle = cactus_surface.get_rect(midbottom = (600, 310))

player_surface = pygame.image.load('Images/Dino/Dino_standing.png')
player_rectangle = player_surface.get_rect(midbottom = (100, 315))

# creating a surface for the font 
text_surface = test_font.render('score', 0, 'Grey25')

# setting up the game loop
while True:
    # checks for any and all events occuring in the loop ...
    for event in pygame.event.get():

        # now if the event is to quit the game, 
        # then quit the game 
        if event.type == pygame.QUIT:
            pygame.quit()       # this statement turns the engine off
                                # but we are still calling for the display.update
                                # this is an issue
            exit()              # So, we need exit here
                # exit is a memeber of a sys lib in python
                # allows to shut down the code itself 

    # blit is used to display a screen on top of other screen.
    # we use it to add images on the display screen 

    # creating the background ..
    screen.blit(background_surface, (0,0))

     # displaying the ground ...
    screen.blit(ground_surface, (0,300))

    # displaying the cactus ...
    screen.blit(cactus_surface, cactus_rectangle)
    cactus_rectangle.left -= 3
    if (cactus_rectangle.left < -100):
        cactus_rectangle.left = width + 100

    # display the score ...
    screen.blit(text_surface, (650, 20))

    # displaying the clouds ...  
    screen.blit(cloud_surface, (60,53))
    screen.blit(cloud_surface, (533,141))

    # displaying the character (dino)
    screen.blit(player_surface, player_rectangle)


    # always at the end of the game loop
    # updates the display ... 
    pygame.display.update()
    
    # adding the celling to the fps of the game at 60 fps
    # this is telling the game to wait atmost ~17 ms before updating
    # the loop cannot be updated any quicker
    clock.tick(60)
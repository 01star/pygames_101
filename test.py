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
test_font = pygame.font.Font(None, 35)

# creating surface for the images 
ground_surface = pygame.image.load('Images/GroundImage.png') 
cloud_surface = pygame.image.load('Images/Clouds.png')

# creating a surface for the font 
text_surface = test_font.render('score', 0, 'Grey30')


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
    # displaying the ground ...
    screen.blit(ground_surface, (0,300))

    # display the score ...
    screen.blit(text_surface, (700, 10))

    # displaying the clouds ...  
    screen.blit(cloud_surface, (60,53))
    screen.blit(cloud_surface, (533,141))

    # always at the end of the game loop
    # updates the display ... 
    pygame.display.update()
    
    # adding the celling to the fps of the game at 60 fps
    # this is telling the game to wait atmost ~17 ms before updating
    # the loop cannot be updated any quicker
    clock.tick(60)
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

# adding a title for the game, screen ...
pygame.display.set_caption('Runner')

# creating a clock, for the framerates and other niche things
clock = pygame.time.Clock()

#setting up the game loop
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

    # draw all the elements up here
    #update everything
    pygame.display.update()
    
    # adding the celling to the fps of the game at 60 fps
    # this is telling the game to wait atmost ~17 ms before updating
    # the loop cannot be updated any quicker
    clock.tick(60)
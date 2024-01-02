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

# the game state flag 
game_active = True

# adding a title for the game, screen ...
pygame.display.set_caption('Runner')

# creating a clock, for the framerates and other niche things
clock = pygame.time.Clock()

# creating a font 
score_font = pygame.font.Font('Fonts/Font.ttf', 20)

# creating surface for the images 
    # .convert_alpha() converts the images into a more workable format for the pygame
    # in theory making our game more optimized ... 
background_surface = pygame.image.load('Images/background.png').convert_alpha()
ground_surface = pygame.image.load('Images/GroundImage.png').convert_alpha()
cloud_surface = pygame.image.load('Images/Clouds.png').convert_alpha()

cactus_surface = pygame.image.load('Images/Cactus/Cactus1.png').convert_alpha()
cactus_rectangle = cactus_surface.get_rect(midbottom = (600, 310))

player_surface = pygame.image.load('Images/Dino/Dino_standing.png')
player_gravity = 0
player_floor = 315
player_rectangle = player_surface.get_rect(midbottom = (100, player_floor))


# creating a surface for the font 
score_surface = score_font.render('score', 0, 'Grey25')

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
            
        # key events --
        # checking for the game state, and sort of making the game resart 
        if event.type == pygame.KEYDOWN and game_active == True:
            if event.key == pygame.K_SPACE:
                if (player_rectangle.bottom == player_floor):
                    player_gravity = -20

        elif event.type == pygame.KEYDOWN and game_active == False:
            game_active = True
            cactus_rectangle = cactus_surface.get_rect(midbottom = (600, 310))
            player_rectangle = player_surface.get_rect(midbottom = (100, player_floor))

        # mouse event --
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if player_rectangle.collidepoint(event.pos):
        #         print ('mosue collision')

    if game_active:
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
        screen.blit(score_surface, (650, 20))

        # displaying the clouds ...  
        screen.blit(cloud_surface, (60,53))
        screen.blit(cloud_surface, (533,141))

        # Player 
        # displaying the character (dino)
        screen.blit(player_surface, player_rectangle)
        player_gravity += 1                         # increase the gravity non-lienarly
        player_rectangle.bottom += player_gravity   # make player fall with that gravity
    
        if (player_rectangle.bottom >= player_floor):
            # if the player is going below the surface
            player_gravity = 0                      # set gravity back to zero
            player_rectangle.bottom = player_floor  # set the player at the floor
        
            
        # checking for the collisions
        if player_rectangle.colliderect(cactus_rectangle):
            game_active = False

    else:
        screen.fill('white')

    # always at the end of the game loop
    # updates the display ... 
    pygame.display.update()
    
    # adding the celling to the fps of the game at 60 fps
    # this is telling the game to wait atmost ~17 ms before updating
    # the loop cannot be updated any quicker
    clock.tick(60)
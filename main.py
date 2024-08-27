# Example file showing a circle moving on screen
import pygame
from trudeau import Trudeau

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#Instantiating Game Objects

#Setup Environment
land = Land(screen)
scenery = pygame.image.load("images/background.png")
tru = Trudeau(pygame, screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    keys = pygame.key.get_pressed()
    tru.move(keys)
    screen.fill("purple")
    tru.update(dt)
    

    land.drawPlatforms(screen)
    land.drawPlatforms(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

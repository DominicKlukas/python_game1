import pygame as pg

"""
Sets up the game environment
"""
class Land(): 
    def __init__(self, screen):
        self.sc = screen
        return


    def drawPlatforms(self, screen): #changed hellow to screen
        pg.draw.rect(screen, "blue", (200, 350, 200, 50)) #changed hellow.sc to screen
        # screen.name = "50"

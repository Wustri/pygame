# Programmer's Block
# Platformer
# Adrian Relloso



# imports go here
import pygame, sys
from pygame.locals import *
from settings import *
from tiles import Tile
from level import Level
from particle import *

# Set Up Window and Pygame stuffs
pygame.init()
iFPS = 32 
fpsClock = pygame.time.Clock()
Screen = pygame.display.set_mode((Screen_Width, Screen_Height), 0, 32)
pygame.display.set_caption('Platformer')

# Using Sound Files
pygame.mixer.pre_init(44100, -16, 2, 2048) 
clrBlack = (0,0,0)

level = Level(Map_Level, Screen)


# GameLoop
RunMe = True
while RunMe: 
	Screen.fill(clrBlack)
    
    # Event pump. Looking for Quit 
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	level.run()

	




	pygame.display.update()
	fpsClock.tick(iFPS)





	
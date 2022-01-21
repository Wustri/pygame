# Programmer's Block
# Platformer
# Adrian Relloso



#Call all the neccesary imports
import pygame, sys, time
from pygame.locals import *

#calls the class, def and variables from the other files
from settings import *
from level import Level
from menu import *
from support import writte_text

# Set Up Window and Pygame stuffs
pygame.init()
iFPS = 32 
fpsClock = pygame.time.Clock()
Screen = pygame.display.set_mode((Screen_Width, Screen_Height), 0, 32)
pygame.display.set_caption('Platformer')


# init the music player
pygame.mixer.pre_init(44100, -16, 2, 2048) 

#setup the black color for the background
clrBlack = (0,0,0)
background = pygame.image.load('assets/background.jpeg')

#init the manu and level scenes as objects
level = Level(Map_Level, Screen)
menu = Menu(Screen)




# GameLoop
RunMe = True
while RunMe: 
	#paint the background
	Screen.blit(background, (0,0))    
    # Event pump. Looking for Quit 
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#if the level class die variable is true the game exits after waiting 5 sec on the you died screen
	if level.die:
		Screen.fill(clrBlack)
		writte_text(Screen,'YOU DIED',1150,400,100,(255,0,0),0,255)
		pygame.display.update()
		time.sleep(5)
		exit()


	#if the menu class level_1 variable is true the level 1 starts
	elif menu.level_1:
		level.run()

	#if ur not dead or playing the game it takes u to the main menu
	else:
		#pass
		menu.run()

	



	#it updates the screen at the specefic framerate
	pygame.display.update()
	fpsClock.tick(iFPS)





	
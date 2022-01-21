#calls the neccesary imports
import pygame

#calls the class, def and variables from the other files
from support import writte_text




class Menu:
    #create all the neccesary variables
    def __init__(self,display) -> None:
        self.display = display
        self.level_1 = False
        self.level_1_buttom = pygame.Rect(450, 500, 250, 75)
        self.die = False

    #draw the title text and a rect as a buttom
    def run(self):
        writte_text(self.display,'Main Menu',1150,400,100,(255,174,82),0,255)
        pygame.draw.rect(self.display, (123,123,123), self.level_1_buttom)


        #check if the buttom is pressed and if you press it start level 1 by changing the variable
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if pygame.Rect.collidepoint(self.level_1_buttom, pygame.mouse.get_pos()):
                    self.level_1 = True




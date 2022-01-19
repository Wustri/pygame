import pygame


from support import writte_text




class Menu:
    def __init__(self,display) -> None:
        self.display = display
        self.level_1 = False
        self.level_1_buttom = pygame.Rect(250, 500, 250, 75)
        self.die = False


    def run(self):
        writte_text(self.display,'Main Menu',750,400,100,(255,174,82),0,255)
        pygame.draw.rect(self.display, (123,123,123), self.level_1_buttom)



        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pygame.Rect.collidepoint(self.level_1_buttom, pygame.mouse.get_pos()):
                    self.level_1 = True




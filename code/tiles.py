#calls the neccesary imports
import pygame
import os 

#calls the class, def and variables from the other files
from support import import_folder
from settings import *

#class to manage the map of the game
class Tile(pygame.sprite.Sprite):
    #import all assets and create all variables and rects
    def __init__(self,pos,folder,image,y) -> None:
        super().__init__()
        self.import_assets()
        self.image = tileset[folder][image]
        self.scaley = 0.48 * y
        self.shifty = 48 - self.scaley
        self.image = pygame.transform.scale(self.image, (48,48))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + self.shifty, 16, self.scaley)
        self.rect.midbottom = self.hitbox.midbottom
        
    #updates the tiles by moving the rects relative to the camera when moving
    #if the h key is pressed the hitboxes are shown
    def update(self,x_camera,Screen):
        self.rect.x -= x_camera
        self.hitbox.x -= x_camera 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_h]:
            pygame.draw.rect(Screen, (0,255,0), self.hitbox,1)

    #load the memory addreses for the images neccesary for the tiles
    def import_assets(self):
        character_path = 'assets/'

        for animation in tileset.keys():
            full_path = character_path + animation
            tileset[animation] = import_folder(full_path)
            







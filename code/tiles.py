import pygame
import os 
from support import import_folder
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,folder,image) -> None:
        super().__init__()
        self.import_assets()
        self.image = tileset[folder][image]
        self.image = pygame.transform.scale(self.image, (48,48))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 16, self.rect.height)
        self.rect.midtop = self.hitbox.midtop
        
    def update(self,x_camera):
        self.rect.x -= x_camera
        self.hitbox.x -= x_camera 
        #pygame.draw.rect(Screen, (0,255,0), self.hitbox,1)

    def import_assets(self):
        character_path = 'assets/'

        for animation in tileset.keys():
            full_path = character_path + animation
            tileset[animation] = import_folder(full_path)
            







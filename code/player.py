import pygame
import os

from pygame.transform import flip
from settings import player_anim
from support import import_folder 
from particle import *





class Player(pygame.sprite.Sprite):
    def __init__(self,pos,Screen) -> None:
        super().__init__()
        self.import_assets()
        self.frame_index = 0 
        self.animation_speed = 0.15
        self.image =  player_anim['idle-01'][self.frame_index]
        self.rect = self.image.get_rect(midtop = pos)
        self.rect.width = 64
        self.rect.height = 64       
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0
        self.gravity_force = 1.3
        self.jump_force = -18
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_hung = False
        self.hung_time = 0
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.on_crouch = False
        self.particles = Particle(Screen)

    def import_assets(self):
        character_path = '../assets/'

        for animation in player_anim.keys():
            full_path = character_path + animation
            player_anim[animation] = import_folder(full_path)
        
    def update(self):
        self.speed = 6
        self.anim() 
        
        self.get_input()
        self.rect.x += self.direction.x * self.speed    
        
    def jump(self):
        self.direction.y = self.jump_force
            
    def gravity(self):
        self.direction.y += self.gravity_force
        self.rect.y += self.direction.y
        
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.on_hung:
            self.jump() 
            self.on_crouch = False
        elif keys[pygame.K_SPACE]:
            pass
            self.on_crouch = False
        elif keys[pygame.K_LSHIFT]:
            self.on_crouch = True
        else:
            self.on_crouch = False
            if self.direction.y < 0:
                self.direction.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0 
        

    def anim(self):
        self.get_status()
        self.particles.emit()
        animation =  player_anim[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index > len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image
        if self.on_crouch == False:
            self.image = pygame.transform.scale(self.image, (64,64))


        if self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)
        
    def get_status(self):
        if self.on_crouch and self.direction.y > 0 and self.direction.y < 0:
            self.status = 'crouch'
            self.image = pygame.transform.scale(self.image, (64,48))
        else:
            self.image = pygame.transform.scale(self.image, (64,64))

        if self.direction.y >= self.gravity_force*2 :
            self.status = 'fall'
        elif self.direction.y <= - self.gravity_force*2 : 
            self.status = 'jump'
        else:
            if self.direction.x != 0 and self.on_ground:
                self.status = 'run'
                for i in range(5):
                    self.particles.add_particles(self.rect.x + 32,self.rect.y + 64)
                
            else:
                if self.on_crouch == False:
                    self.status = 'idle-01'
        




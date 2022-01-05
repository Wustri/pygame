import pygame
from settings import enemy_anim
from support import import_folder


class Enemy:
    def __init__(self,pos) -> None:
        super().__init__()
        self.import_assets()
        self.frame_index = 0 
        self.animation_speed = 0.15
        self.image =  enemy_anim['enemy_green'][self.frame_index]
        self.rect = self.image.get_rect(midtop = pos)
        self.rect.width = 64
        self.rect.height = 64       
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0
        self.pos = pos
        

    def update(self,x_camera):
        self.rect.x -= x_camera

    def import_assets(self):
        character_path = '../assets/'

        for animation in enemy_anim.keys():
            full_path = character_path + animation
            enemy_anim[animation] = import_folder(full_path)
    
    def draw(self,screen):
        pygame.Surface.blit(self.image, screen, self.pos)







    """def x_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed 

        for sprite in self.tiles.sprites():
            if sprite.hitbox.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.hitbox.right 
                elif player.direction.x > 0:
                    player.rect.right  = sprite.hitbox.left 

    def y_collision(self):
        player = self.player.sprite
        player.gravity()
        player.hung_time += 1
         

        for sprite in self.tiles.sprites():
            if sprite.hitbox.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.hitbox.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.on_hung = True
                    player.hung_time = -5
                    
                    
                elif player.direction.y < 0:
                    player.rect.top = sprite.hitbox.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.om_ceiling = False
        if player.on_hung == True:
            if player.hung_time < 0:
                player.on_hung = True
            else:
                player.on_hung = False"""
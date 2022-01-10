import pygame
from pygame import sprite
from tiles import Tile
from settings import *
from player import *
from support import *
from enemies import *


camera = 0


class Level:
    def __init__(self,level_data,Surface) -> None:
        self.display_surface = Surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.enemy = pygame.sprite.Group()
        
        

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.camera_movement()


        x = Tile_Size*6
        y =Tile_Size*6
        
    


        self.player.update()
        self.x_collision()
        self.y_collision()
        self.player.draw(self.display_surface)
        self.Hud()
        

    def x_collision(self):
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
                player.on_hung = False
                    

    def setup_level(self,layout):
        
        self.tiles = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_num,row in enumerate(layout):
            for col_num,col in enumerate(row):
                if col == 'T':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',1)    
                    self.tiles.add(tile)
                if col == 'L':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',1)
                    self.tiles.add(tile)
                if col == 'R':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',1)
                    self.tiles.add(tile)
                if col == 'X':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',1)
                    self.tiles.add(tile)
                if col == 'W':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',0)
                    self.tiles.add(tile)
                if col == 'E':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',1)
                    self.tiles.add(tile)
                if col == 'P':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    player_sprite = Player((x,y),self.display_surface)
                    self.player.add(player_sprite)
                
                
    def camera_movement(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        keys = pygame.key.get_pressed()

       
        if player_x > (Screen_Width*3)/4 and direction_x > 0:
            self.world_shift = 10
            player.speed = 0
        elif player_x < Screen_Width/4 and direction_x < 0:
            self.world_shift = -10
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

    def Hud(self):
        writte_text(self.display_surface,'lives',100,200,32,(255,0,0),0,255)

        

    
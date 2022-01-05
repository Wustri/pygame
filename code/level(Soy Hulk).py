import pygame
from pygame import sprite
from tiles import Tile
from settings import *
from player import *


camera = 0


class Level:
    def __init__(self,level_data,Surface) -> None:
        self.display_surface = Surface
        self.setup_level(level_data)
        self.world_shift = 0
        

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.camera_movement()


        self.player.update()
        self.x_collision()
        self.y_collision()
        self.player.draw(self.display_surface)
        

    def x_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed 

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    sprite.rect.right =  player.rect.left + 16
                elif player.direction.x > 0:
                    sprite.rect.left = player.rect.right + 16
    
    def y_collision(self):
        player = self.player.sprite
        player.gravity()
         

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    #Player.touching_floor == False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    #Player.touching_floor == False

    def setup_level(self,layout):
        character_path = '../assets'
        #self.layout = layout
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_num,row in enumerate(layout):
            for col_num,col in enumerate(row):
                if col == 'T':
                    x = 64*col_num
                    y =64*row_num
                    tile = Tile((x,y),'grass_tiles',17)    
                    self.tiles.add(tile)
                if col == 'L':
                    x = 64*col_num
                    y =64*row_num
                    tile = Tile((x,y),'grass_tiles',18)
                    self.tiles.add(tile)
                if col == 'R':
                    x = 64*col_num
                    y =64*row_num
                    tile = Tile((x,y),'grass_tiles',15)
                    self.tiles.add(tile)
                if col == 'X':
                    x = 64*col_num
                    y =64*row_num
                    tile = Tile((x,y),'grass_tiles',5)
                    self.tiles.add(tile)
                if col == 'W':
                    x = 64*col_num
                    y =64*row_num
                    tile = Tile((x,y),'grass_tiles',0)
                    self.tiles.add(tile)
                if col == 'E':
                    x = 64*col_num
                    y =64*row_num
                    tile = Tile((x,y),'grass_tiles',2)
                    self.tiles.add(tile)
                if col == 'P':
                    x = 64*col_num
                    y =64*row_num
                    player_sprite = Player((x,y),self.display_surface)
                    self.player.add(player_sprite)
                
    def camera_movement(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        keys = pygame.key.get_pressed()

       
        if player_x > (Screen_Width*3)/4 and direction_x > 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x < Screen_Width/4 and direction_x < 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8


    
    
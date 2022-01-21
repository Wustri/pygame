#calls the neccesary imports
import pygame
from pygame import sprite

#calls the class, def and variables from the other files
from tiles import Tile
from settings import *
from player import *
from support import *



#main class that runs the entire level
class Level:
    #create all the necessary variables
    def __init__(self,level_data,Surface) -> None:
        self.display_surface = Surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.enemy = pygame.sprite.Group()
        self.die = False
        
        
    #def to update and draw all classes
    #if h key is presses all hitboxes are shown for debugging purposes
    def run(self):
        keys = pygame.key.get_pressed()
        self.tiles.update(self.world_shift,self.display_surface)
        self.spikes.update(self.world_shift,self.display_surface)
        self.player.update()
        self.x_collision()
        self.y_collision()
        self.camera_movement()
        if keys[pygame.K_h] == False:
            self.tiles.draw(self.display_surface)
            self.spikes.draw(self.display_surface)
        self.Hud()
        self.player.draw(self.display_surface)
        
        
    #def that manages the collisions on the x axis
    def x_collision(self):
        player = self.player.sprite
        #move the player rect right before making the collision so that it doesnt clip
        player.rect.x += player.direction.x * player.speed 

        #if the player collides with a tile checks the direction the player is moving and
        #moves the player to the side so that it doesnt get inside the tile
        for sprite in self.tiles.sprites():
            if sprite.hitbox.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.hitbox.right 
                elif player.direction.x > 0:
                    player.rect.right  = sprite.hitbox.left 

        for sprite in self.spikes.sprites():
            if sprite.hitbox.colliderect(player.rect):
                player.hit()

    #def that manages the collisions on the y axis
    def y_collision(self):
        player = self.player.sprite
        player.gravity()
        player.hung_time += 1
         
        #if the player collides with a tile checks the direction the player is moving and
        #moves the player to the side so that it doesnt get inside the tile
        for sprite in self.tiles.sprites():
            if sprite.hitbox.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.hitbox.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.on_hung = True
                    player.hung_time = -5
                    
                #cotrol the colision with the floor and eliminate the gravity so that it doesnt acumulate and go throgh the floor
                elif player.direction.y < 0:
                    player.rect.top = sprite.hitbox.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        #change the variable depending if it is touching the floor or the ceiling and adds a timer called on hung to give the player
        #a time to make it easier to jump on edges and make the game feel better
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
        if player.on_hung == True:
            if player.hung_time < 0:
                player.on_hung = True
            else:
                player.on_hung = False


                
                    
    #def to set up all the tiles for the map
    def setup_level(self,layout):
        #create the sprite groups for the tiles and player
        self.tiles = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        #repeat this for for each cell in the grip map
        for row_num,row in enumerate(layout):
            for col_num,col in enumerate(row):
                
                #deppending on the letter the layout has in that coordinate place a different tile
                if col == 'T':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',5,100)    
                    self.tiles.add(tile)
                if col == 'L':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',10,100)
                    self.tiles.add(tile)
                if col == 'R':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',1,100)
                    self.tiles.add(tile)
                if col == 'X':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',0,100)
                    self.tiles.add(tile)
                if col == 'W':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',0,100)
                    self.tiles.add(tile)
                if col == 'E':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',0,100)
                    self.tiles.add(tile)
                if col == 'O':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',3,100)
                    self.tiles.add(tile)
                if col == 'U':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',0,100)
                    self.tiles.add(tile)
                if col == 'G':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',4,100)
                    self.tiles.add(tile)
                if col == 'N':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',5,100)
                    self.tiles.add(tile)
                if col == 'H':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    tile = Tile((x,y),'grass_tiles',6,100)
                    self.tiles.add(tile)
                if col == 'S':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    spike = Tile((x,y),'extra_tiles',0,50)
                    self.spikes.add(spike)
                    #place the player
                if col == 'P':
                    x = Tile_Size*col_num
                    y =Tile_Size*row_num
                    player_sprite = Player((x,y),self.display_surface)
                    self.player.add(player_sprite)
                
    #move the camera when the player passes 1/4 of the screen to each side
    def camera_movement(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x > (Screen_Width*3)/4 and direction_x > 0:
            self.world_shift = 10
            player.speed = 0
        elif player_x < Screen_Width/4 and direction_x < 0:
            self.world_shift = -10
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

    #draw the hud to know how many lives we have and update the die variable
    def Hud(self):
        player = self.player.sprite
        writte_text(self.display_surface,'lives',100,200,32,(255,0,0),0,255)
        writte_text(self.display_surface, str(player.lives) ,250,200,32,(255,0,0),0,255)
        self.die = player.die
        

        

    
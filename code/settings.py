#calls the neccesary imports
import pygame


#create all the neccessary variables and dictionary
Map_Level = [
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '   GNH GH O         ',
    '      P             ',
    '             O      ',
    '     GNNNNH GTH GH GNNNNNNNNNNNNNH',
    '    LX              ',
    '   LXX              ',
    'O                      SSSSS',
    'TT     O     L R    ',
    '  O    O    LE WR   ',
    '     O     LXE WXR           SSSS      ',
    'TTTTTTTTTTTTTE WTTTTTTTTTTTTTTTTTTTTTTTTT',
]

Tile_Size = 48
Screen_Height = len(Map_Level) * Tile_Size
Screen_Width = 1200
player_anim = {'idle-01':[],'run':[],'jump':[],'fall':[],'crouch':[]}
Sound = {'sounds':[]}
enemy_anim = {'enemy_green':[]}
tileset = {'tiles': [],'grass_tiles':[],'extra_tiles':[]}
Screen = pygame.display.set_mode((Screen_Width, Screen_Height), 0, 32)



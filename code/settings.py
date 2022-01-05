import pygame

Map_Level = [
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '   TTT TT T         ',
    '      P             ',
    '             T      ',
    '     LTTTTT TXT TT T',
    '    LX              ',
    '   LXX              ',
    'T                   ',
    'XT     T     L R    ',
    '  T    X    LE WR   ',
    '     F     LXE WXR B',
    'TTTTTTTTTTTXXE WXXTX',
]

Tile_Size = 48
Screen_Height = len(Map_Level) * Tile_Size
Screen_Width = 1200
player_anim = {'idle-01':[],'run':[],'jump':[],'fall':[],'crouch':[]}
enemy_anim = {'enemy_green':[]}
tileset = {'tiles': [],'grass_tiles':[]}
Screen = pygame.display.set_mode((Screen_Width, Screen_Height), 0, 32)



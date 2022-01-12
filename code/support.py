from os import walk
import pygame



def import_folder(path):
    images_list = []
    for _,__,files in walk(path):
        sorted_files = sorted(files)
        print(sorted_files)
        for images in sorted_files:
            if images != '.DS_Store':
                full_path = path + '/' + images 
                image_load = pygame.image.load(full_path)
                images_list.append(image_load) 
                #print(full_path)
    return images_list

def writte_text(display,text_to_render,X,Y,Size,text_color, background_color,alpha):
    #self.display_surface = display

    font = pygame.font.Font('freesansbold.ttf', Size)
    if background_color == 0:
        text = font.render(text_to_render, True, text_color)
    else:
        text = font.render(text_to_render, True, text_color, background_color)
    text.set_alpha(alpha)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    display.blit(text, textRect)
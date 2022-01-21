#calls the neccesary imports
from os import walk
import pygame


#def to import memory addreses of images from a specific folder named after a key from a dictionary into the same dictionary
def import_folder(path):
    #create a temp list
    images_list = []
    #get all the files from the path to the folder with the name of the key you specified
    for _,__,files in walk(path):
        #sort alphanumerically all files to have some order 
        sorted_files = sorted(files)
        #for each file in the folder
        for images in sorted_files:
            #is the file is named .DS_Store ignore it
            if images != '.DS_Store':
                #add the name of the file to the previous path to get the full path to the file
                full_path = path + '/' + images 
                #get the memory addres of the loaded files
                image_load = pygame.image.load(full_path)
                #append the memory addres into the list
                images_list.append(image_load) 
    #return the list with memory addreses
    return images_list

#Same as the one on top just changed a line to load the files as sounds and not like images
def import_sounds(path):
    images_list = []
    for _,__,files in walk(path):
        sorted_files = sorted(files)
        #print(sorted_files)
        for images in sorted_files:
            if images != '.DS_Store':
                full_path = path + '/' + images 
                image_load = pygame.mixer.Sound(full_path)
                images_list.append(image_load) 
    return images_list

#a def to work better with texts in a only line with all the parameter you would want to use
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
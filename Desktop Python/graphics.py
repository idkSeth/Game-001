import os
import pygame 

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

def display_t_text(text, size, position):
    pass

def display_text(text:str, size:int, position:tuple):
    font = pygame.font.Font(r"Dependencies/font.ttf", size)
    img = font.render(text, True, (52, 226, 226))
    screen.blit(img, position)
    pygame.display.flip()

def display_term_c(size:int, position:tuple):
    rect = Rect(position, size)
    if event.type == KEYDOWN:
        if event.key == K_BACKSPACE:
            if len(text)>0:
                text = text[:-1]
        else:
            text += event.unicode

def get_user_text():
    pass
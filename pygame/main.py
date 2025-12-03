import sys, pygame
from pygame.locals import *
from functions import solo_gamemode

pygame.init()

FONT = pygame.font.SysFont('Comic Sans MS', 30)
SIZE = width, height = 640, 480
SCREEN = pygame.display.set_mode(SIZE)
BCK_COLOR = (255, 255, 255)
SCREEN.fill(BCK_COLOR)

pygame.display.set_caption("TicTacToe")
pygame.draw.rect(SCREEN, (28, 28, 107), (190, 400, 250, 50) )

clickable_area_solo = pygame.Rect((190, 300), (250, 50))
rect_solo_mode = pygame.Surface(clickable_area_solo.size)
rect_solo_mode.fill((178, 0, 0))

clickable_area_multi = pygame.Rect((190, 400), (250, 50))
rect_multi_mode = pygame.Surface(clickable_area_solo.size)
rect_multi_mode.fill((28, 28, 107))

SCREEN.blit(rect_solo_mode, (190, 300))
SCREEN.blit(rect_multi_mode, (190, 400))

text_surface = FONT.render('Mode 1 joueur', False, (0, 0, 0))
SCREEN.blit(text_surface, (220,300))

text_surface = FONT.render('Mode 2 joueurs', False, (0, 0, 0))
SCREEN.blit(text_surface, (205,400))


continue_game = True

pygame.display.flip()

while continue_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continue_game = False

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1: 
                if clickable_area_solo.collidepoint(event.pos):
                    solo_gamemode.solo_gamemode_screen(SCREEN, BCK_COLOR)
                    
                    
        

pygame.quit()
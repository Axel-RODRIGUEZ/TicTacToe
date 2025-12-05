import sys, pygame
from pygame.locals import *

class solo_gamemode:
    def solo_gamemode_screen(screen, color):
        lines_color = (0, 0, 0)

        screen.fill(color)
        pygame.display.flip()
        pygame.draw.line(screen, lines_color, (200, 100), (200, 400), 10 )
        pygame.display.flip()

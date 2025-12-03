import sys, pygame
pygame.init()

SIZE = width, height = 640, 480
my_font = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode(SIZE)
color = (255, 255, 255)
screen.fill(color)

pygame.display.set_caption("TicTacToe")

pygame.draw.rect(screen, (178, 0, 0), (190, 300, 250, 50) )
pygame.draw.rect(screen, (28, 28, 107), (190, 400, 250, 50) )

image = pygame.image.load('pygame\\images\\TicTacToe logo.png').convert()
image = pygame.transform.scale(image, (200, 220))
screen.blit(image, (220, 30))

text_surface = my_font.render('Mode 1 joueur', False, (0, 0, 0))
screen.blit(text_surface, (220,300))

text_surface = my_font.render('Mode 2 joueurs', False, (0, 0, 0))
screen.blit(text_surface, (205,400))

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
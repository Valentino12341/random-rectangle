import pygame 
from random import randint
pygame.init()
HEIGHT = 500
WIDHT = 500
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption('rect display')

WHITE = (255,255,255)
BLACK= (0,0,0)


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def display(self, screen):

        pygame.draw.rect(screen, BLACK, (100, 100, self.width, self.length))
        

Rect = Rectangle(randint(10,1000), randint(10,1000))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    Rect.display(screen)

    pygame.display.update()


pygame.quit()






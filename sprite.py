import pygame
import random


pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("catch me!")


while True:
    colour=(random.randint(0,250),random.randint(0,250),random.randint(0,250))
    colour1=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    colour2=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()



    screen.fill((colour))
    pygame.draw.rect(screen,colour1,(150,230,100,100))
    pygame.draw.circle(screen,colour2,(150,150),50)
    pygame.time.delay(800)
    pygame.display.flip()
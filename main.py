import pygame,sys
from spaceship import Spaceship

pygame.init()

grey = (29, 29, 27)
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700


screen = pygame.display.set_mode((750, 700))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #Update
    spaceship_group.update()


    #Drawing       
    screen.fill(grey)  
    spaceship_group.draw(screen)
    spaceship_group.sprite.lasers_group.draw(screen) 

    pygame.display.update()
    clock.tick(60)
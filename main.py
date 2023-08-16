import pygame
import settings
from water import Water

pygame.init()
pygame.display.set_caption("Waves in pygame - SorenDev")
screen: pygame.Surface = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

water: Water = Water((0, 700), (settings.WIDTH, 700), 70, 10)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(settings.BLACK)
            
    water.draw(screen)
            
    pygame.display.update()
    pygame.time.Clock().tick(settings.FPS)
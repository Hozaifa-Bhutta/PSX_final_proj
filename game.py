import pygame
from make_platform import platform
pygame.init()
WIDTH = 1200
HEIGHT = 1000
BLUE = (0,0,220)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
platforms = pygame.sprite.Group()
platform1 = platform(BLUE, 20, 20, 30, 30, screen)
platforms.add(platform1)
 
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	presed = pygame.key.get_pressed()
	pygame.display.flip()
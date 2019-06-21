import pygame
import platform
pygame.init()
WIDTH = 1200
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
platforms = pygame.sprite.Group()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill((0,0,200))
	platforms.add(platform((0,200,0),50,50))
	presed = pygame.key.get_pressed()
	pygame.display.flip()
import pygame
from make_platform import platform
from make_player import player
clock = pygame.time.Clock()

pygame.init()
WIDTH = 1200
HEIGHT = 1000
BLUE = (0,0,220)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
platforms = pygame.sprite.Group()
pygame.Rect(10,10,10,10)
platform1 = platform(BLUE, 20, 20, 30, 30, screen)
platforms.add(platform1)
player1 = player(100,10,screen)
 
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		player1.jump()
	if pressed[pygame.K_RIGHT]:
		player1.go_right()
	if pressed[pygame.K_LEFT]:
		player1.go_left()
	screen.fill((0,0,0))
	for platform in platforms:
		platform.draw_wall()
	player1.draw_player()

	pygame.display.flip()
	clock.tick(60)

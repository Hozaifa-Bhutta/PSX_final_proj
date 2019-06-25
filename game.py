import pygame
from make_platform import platform
from make_player import player

clock = pygame.time.Clock()

pygame.init()
WIDTH = 1200
HEIGHT = 600
BLUE = (0,0,220)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
platforms = pygame.sprite.Group()
pygame.Rect(10,10,10,10)
platform1 = platform(BLUE, 100, 20, 450, 400, screen)
platforms.add(platform1)
player1 = player(100,500,screen,platforms)
 
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		for i in range(0,5):
			for platform in platforms:
				if player1.rect.colliderect(platform.rect):
					break
				else:
					player1.jump()
	if pressed[pygame.K_RIGHT]:
		player1.go_right()
	if pressed[pygame.K_LEFT]:
		player1.go_left()

	
	for platform in platforms:
		if player1.rect.colliderect(platform.rect):
			break
		else:
			player1.gravity()
	if player1.jumping == True:
		player1.jump()
	screen.fill((0,0,0))
	for platform in platforms:
		platform.draw()
		platform.update()
	player1.draw_player()
	player1.rect.x-=1


	pygame.display.flip()
	clock.tick(60)

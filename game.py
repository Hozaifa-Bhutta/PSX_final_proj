import pygame
from make_platform import platform
from make_player import player
def is_colliding(platform, player):
		if player.rect.colliderect(platform.rect):
			platform_list = range(platform.rect.y-10,platform.rect.y+10)
			if (player1.rect.y-30) ==(platform.rect.y-platform.rect.height):
				return 'Up'
			if (player1.rect.y +50) in platform_list:
				return 'Down'

clock = pygame.time.Clock()

pygame.init()
WIDTH = 1200
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
platforms = pygame.sprite.Group()
pygame.Rect(10,10,10,10)
platform1 = platform(BLUE, 100, 20, 450, 400, screen)
platforms.add(platform1)
player1 = player(100,500,screen,platforms)
 
while not done:
	previous_y = player1.rect.y
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		for i in range(0,5):
			for platform in platforms:
				if is_colliding(platform,player1) == 'Up':
					print ('Don\'t go up')
				else:
					player1.jump()

				

		player1.jumping == False
	if pressed[pygame.K_RIGHT]:
		player1.go_right()
	if pressed[pygame.K_LEFT]:
		player1.go_left()

	
	for platform in platforms:
		if is_colliding(platform,player1) == 'Down':
			print ('Dont go down')
		else:
			player1.gravity()

	screen.fill((0,0,0))
	for platform in platforms:
		platform.draw()
		platform.update()
	player1.draw_player()
	player1.rect.x-=1


	pygame.display.flip()
	clock.tick(60)

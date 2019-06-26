import pygame
from make_platform import platform
from make_player import player
def is_colliding(platforms, player):
	for platform in platforms:	
		if player.rect.colliderect(platform.rect):
			platform_list_y = range(platform.rect.y-10,platform.rect.y+10)
			if (player.rect.y-30) ==(platform.rect.y-platform.rect.height):
				#print ('Up')
				return 'Up'
			if (player.rect.y +55) in platform_list_y:
				#print ('Down')
				return 'Down'
			if abs((platform.rect.x)-(player.rect.x + 40)) <=5: 
				print ('in right')
				return 'Right'
			if abs((player.rect.x)-(platform.rect.x+platform.width)):
				return 'Left'
	print (abs(platform.rect.x-(player.rect.x+40)))

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
platforms.add(platform(GREEN, 200, 200 ,800, 300,screen))
player1 = player(100,500,screen,platforms)
while not done:

	previous_y = player1.rect.y
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		for i in range(0,5):
			if is_colliding(platforms,player1) == 'Up':
				#print ('Don\'t go up')
				pass
			else:
				player1.jump()

				

		player1.jumping == False
	if pressed[pygame.K_RIGHT]:
		if is_colliding(platforms,player1) == 'Right':
			#print ('Don\'t go right')
			pass
		else:
			player1.go_right()

	if pressed[pygame.K_LEFT]:
		if is_colliding(platforms,player1) == 'Left':
			#print ('don\'t go left')
			pass
		else:
			player1.go_left()

	
	if is_colliding(platforms,player1) == 'Down':
		#print ('Dont go down')

		player1.velocity = 1
	else:
		player1.gravity()

	screen.fill((0,0,0))
	for platform in platforms:
		platform.draw()
		platform.update()
	player1.draw_player()
	#player1.rect.x-=1


	pygame.display.flip()
	clock.tick(60)

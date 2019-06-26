import pygame
from make_platform import platform
from make_player import player
from make_lava import lava as lv
def is_colliding(platforms, player):
	i = 0
	direction_vals = []
	for platform in platforms:	
		i += 1
		if player.rect.colliderect(platform.rect):
			platform_list_y = range(platform.rect.y-10,platform.rect.y+10)
			if i %2 == 0:
				print (platform.rect.y-platform.rect.height,player.rect.y-30)
			if (player.rect.y-34) ==(platform.rect.y-platform.height):
				#print ('Up')
				direction_vals.append('Up')
			if (player.rect.y +55) in platform_list_y:
				#print ('Down')
				direction_vals.append('Down')
			if abs((platform.rect.x)-(player.rect.x + 40)) <=5: 
				direction_vals.append('Right')
			if abs((player.rect.x)-(platform.rect.x+platform.width)):
				direction_vals.append('Left')
	return direction_vals

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
platforms.add(platform(BLUE,100,20,800,250,screen))
platforms.add(platform(GREEN, 100, 20 ,800, 300,screen))
player1 = player(100,500,screen,platforms)
Lava = lv(RED,500,700,-400,1,screen) 
while not done:

	previous_y = player1.rect.y
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		for i in range(0,5):
			if 'Up' in is_colliding(platforms,player1):
				#print ('Don\'t go up')
				pass
			else:
				player1.jump()

				

		player1.jumping == False
	if pressed[pygame.K_RIGHT]:
		if 'Right' in is_colliding(platforms,player1):
			#print ('Don\'t go right')
			pass
		else:
			player1.go_right()

	if pressed[pygame.K_LEFT]:
		if 'Left' in is_colliding(platforms,player1) :
			#print ('don\'t go left')
			pass
		else:
			player1.go_left()

	
	if 'Down' in is_colliding(platforms,player1):
		#print ('Dont go down')

		player1.velocity = 1
	else:
		player1.gravity()


	screen.fill((0,0,0))
	for platform in platforms:
		platform.draw()
		platform.update()
	if player1.rect.colliderect(Lava.rect):
		print ('You lose')
	Lava.update_lava()

	player1.draw_player()
	Lava.draw_lava()
	if 'Left' in is_colliding(platforms,player1):
		#print ('don\'t go left')
		pass
	else:
		player1.rect.x-=1
	if 'Right' in is_colliding(platforms,player1):
		pass
	else:
		player1.rect.x -=1
	


	pygame.display.flip()
	clock.tick(60)

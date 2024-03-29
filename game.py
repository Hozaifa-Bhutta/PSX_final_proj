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
			if (player.rect.y-34) ==(platform.rect.y-platform.height):
				#print ('Up')
				direction_vals.append('Up')
			elif (player.rect.y +55) in platform_list_y:
				#print ('Down')
				direction_vals.append('Down')
			elif abs((platform.rect.x)-(player.rect.x + 40)) <=5: 
				direction_vals.append('Right')
			elif abs((player.rect.x)-(platform.rect.x+platform.width)):
				direction_vals.append('Left')
	return direction_vals
def game_over(screen):
	font = pygame.font.Font(None, 36)
	text = font.render("Game Over", True, RED)
	text_rect = text.get_rect()
	text_x = screen.get_width() / 2 - text_rect.width / 2
	text_y = screen.get_height() / 2 - text_rect.height / 2
	screen.blit(text, [text_x, text_y])
def Win(screen):
	font = pygame.font.Font(None, 36)
	text = font.render("You Win", True,GREEN)
	text_rect = text.get_rect()
	text_x = screen.get_width() / 2 - text_rect.width / 2
	text_y = screen.get_height() / 2 - text_rect.height / 2
	screen.blit(text, [text_x, text_y])

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
platforms.add(platform(BLACK,100,500,1000,500,screen))
platforms.add(platform(BLUE,100,20,800,250,screen))
platforms.add(platform(GREEN, 100, 20 ,800, 300,screen))
platforms.add(platform(WHITE, 200, 20 ,60, 400,screen))
platforms.add(platform(BLACK, 100, 20 ,75, 350,screen))
platforms.add(platform(BLUE, 200, 20 ,400, 300,screen))
platforms.add(platform(GREEN, 150, 20 ,400, 300,screen))
platforms.add(platform(BLACK, 250, 20 ,206, 300,screen))

platforms.add(platform(WHITE, 300, 20 ,400, 400,screen))
platforms.add(platform(RED, 100, 20 ,300, 350,screen))
platforms.add(platform(BLUE, 210, 20 ,500, 300,screen))
platforms.add(platform(BLACK, 150, 20 ,550, 300,screen))
platforms.add(platform(BLUE, 250, 20 ,1000, 300,screen))

platforms.add(platform(BLUE, 200, 20 ,480, 200,screen))
platforms.add(platform(GREEN, 100, 20 ,400, 100,screen))
platforms.add(platform(BLACK, 200, 20 ,300, 150,screen))
platforms.add(platform(BLACK, 150, 20 ,400, 50,screen))
platforms.add(platform(RED, 250, 20 ,500, 100,screen))

platforms.add(platform(RED,100,20,1800,250,screen))
platforms.add(platform(GREEN, 100, 20 ,1800, 300,screen))
platforms.add(platform(WHITE, 200, 20 ,1600, 400,screen))
platforms.add(platform(BLACK, 100, 20 ,1705, 350,screen))
platforms.add(platform(BLUE, 200, 20 ,1400, 300,screen))
platforms.add(platform(WHITE, 150, 20 ,1400, 300,screen))
platforms.add(platform(BLACK, 250, 20 ,1206, 300,screen))

platforms.add(platform(BLUE, 300, 20 ,1400, 400,screen))
platforms.add(platform(RED, 100, 20 ,1300, 350,screen))
platforms.add(platform(BLACK, 210, 20 ,1500, 300,screen))
platforms.add(platform(RED, 150, 20 ,1550, 300,screen))
platforms.add(platform(GREEN, 250, 20 ,1500, 300,screen))

platforms.add(platform(WHITE, 200, 20 ,1480, 200,screen))
platforms.add(platform(BLACK, 100, 20 ,1400, 100,screen))
platforms.add(platform(RED, 200, 20 ,1300, 150,screen))
platforms.add(platform(BLUE, 150, 20 ,1400, 50,screen))
platforms.add(platform(BLACK, 250, 20 ,1500, 100,screen))
platforms.add(platform(BLACK,100,100,1500,500,screen))
platforms.add(platform(BLACK,20,1000, 1800, 0, screen))

platforms.add(platform(BLUE,50,20,2000,450,screen))
platforms.add(platform(GREEN,20,100,2100,550,screen))
platforms.add(platform(RED,100,20,2050,50,screen))
platforms.add(platform(WHITE,20,98,1900,200,screen))
platforms.add(platform(BLACK,50,10,2100,10,screen))
platforms.add(platform(BLACK,10,1000,2000,-900,screen))

platforms.add(platform(WHITE, 300, 20 ,2400, 400,screen))
platforms.add(platform(RED, 100, 20 ,2350, 230,screen))
platforms.add(platform(BLUE, 210, 20 ,2500, 230,screen))
platforms.add(platform(BLACK, 150, 20 ,2550, 2300,screen))
platforms.add(platform(BLUE, 250, 20 ,2300, 230,screen))

platforms.add(platform(WHITE, 200, 20 ,2480, 240,screen))
platforms.add(platform(BLACK, 100, 20 ,2400, 270,screen))
platforms.add(platform(RED, 200, 20 ,2300, 290,screen))
platforms.add(platform(BLUE, 150, 20 ,2400, 240,screen))
platforms.add(platform(BLACK, 250, 20 ,2500, 250,screen))
platforms.add(platform(BLACK,100,100,2700,250,screen))
platforms.add(platform(BLACK,20,1000, 2800, 200, screen))

platforms.add(platform(BLUE, 200, 20 ,2480,200,screen))
platforms.add(platform(GREEN, 100, 20 ,2400, 200,screen))
platforms.add(platform(BLACK, 200, 20 ,2900, 400,screen))
platforms.add(platform(BLACK, 150, 20 ,2400, 210,screen))
platforms.add(platform(RED, 250, 20 ,2800, 300,screen))

platforms.add(platform(BLACK,200,1100,3500,300,screen))
platforms.add(platform(BLUE,200,20,3300,400,screen))
platforms.add(platform(BLUE,10,10,3500,100,screen))
platforms.add(platform(GREEN,300,20,3550,200,screen))
platforms.add(platform(BLACK,250,20,3650,150,screen))
platforms.add(platform(BLACK,10,240,4100,-20,screen))
platforms.add(platform(BLUE,10,20,4000,350,screen))
platforms.add(platform(GREEN,120,20,4460,235,screen))
#Wrong path
platforms.add(platform(RED,750,10,5000,500,screen))
platforms.add(platform(RED,20,10,5900,540,screen))
platforms.add(platform(BLACK,40,1300,6000,200,screen))
#Right path
platforms.add(platform(RED,750,10,5000,100,screen))
platforms.add(platform(BLUE,10,10,6050,220,screen))
platforms.add(platform(BLUE,10,10,6200,220,screen))
platforms.add(platform(BLUE,10,10,6350,220,screen))
platforms.add(platform(BLUE,10,10,6550,220,screen))
platforms.add(platform(BLUE,10,10,6750,220,screen))
platforms.add(platform(BLACK,100,500,6800,350,screen))
game_win = False

castle = pygame.image.load('castle.png')
castle_rect = castle.get_rect()
player1 = player(200,500,screen,platforms)
Lava = lv(RED,500,700,-400,1,screen) 
moving = True
castle_rect.x += 7000
castle_rect.y+=400
button = pygame.Rect(WIDTH/2, HEIGHT/2, 100, 50)
start = False
while not done:

	if start:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		if moving == True:
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
			#print ('You lose')
			game_over(screen)
			pressed = None
			moving = False
		Lava.update_lava()
		#pygame.draw.rect(screen,GREEN,castle_rect)
		
		#castle_rect.y = 300
		screen.blit(castle, castle_rect)
		player1.draw_player()
		Lava.draw_lava()
		

		if 'Left' in is_colliding(platforms,player1):
			#print ('don\'t go left')
			pass
		elif game_win != True:
			player1.rect.x-=1
		if 'Right' in is_colliding(platforms,player1):
			pass
		elif game_win != True:
			player1.rect.x -=1
		if game_win != True:
			castle_rect.x -= 1
		if player1.rect.x >= WIDTH-20:
					player1.rect.x = WIDTH-20
		if player1.rect.colliderect(castle_rect):
			Win(screen)
			pressed = None
			moving = False 
			game_win = True
	else:
		mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],10,10)
		screen.fill((0,0,0))
		pygame.draw.rect(screen,BLACK,button)
		font = pygame.font.Font(None, 36)
		text = font.render("Start", True, WHITE)
		text_rect = text.get_rect()
		text_x =  button.x + 25
		text_y = button.y + 25
		screen.blit(text, [text_x, text_y])

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if mouse_rect.colliderect(button):
					start = True

	pygame.display.flip()
	clock.tick(60)

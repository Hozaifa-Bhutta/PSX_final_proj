import pygame

class player(pygame.sprite.Sprite):
	def __init__(self,x,y,screen):

		super().__init__()
		
		RED = (255, 0, 0)
		self.color = RED
		self.width = 40
		self.height = 60
		self.x = x
		self.y = y
		self.screen = screen
		self.rect = pygame.Rect(self.x,self.y,40,60)
	def draw_player(self):
		pygame.draw.rect(self.screen,self.color, self.rect)
	
	def jump(self):
		 for x in range(11):
		 	self.y -= 1

	def go_left(self):
		self.x += -6
 
	def go_right(self):
		print ('In go_right')
		self.x += 6
		print (self.rect)

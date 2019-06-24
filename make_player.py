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
		self.speed = 1
	def draw_player(self):
		pygame.draw.rect(self.screen,self.color, self.rect)
	
	def gravity(self):
		pass

	def jump(self):
		for x in range(1,11):
			self.rect.y -= 1

	def go_left(self):
		self.rect.x += -6
 
	def go_right(self):
		self.rect.x += 6

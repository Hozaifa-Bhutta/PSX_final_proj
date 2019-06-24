import pygame

class player(pygame.sprite.Sprite):
	def __init__(self,x,y):

		super().__init__()
		
		RED = (255, 0, 0)

		self.width = 40
		self.height = 60
		self.x = x
		self.y = y
		self.image = pygame.Surface([width, height])
		self.image.fill(RED)
	def draw_player(self):
		pygame.draw.rect(self.x,self.y,self.width,self.height)
		
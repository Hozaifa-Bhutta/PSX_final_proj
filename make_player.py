import pygame

class player(pygame.sprite.Sprite):
	def __init__(self):

		super().__init__()
		
		RED = (255, 0, 0)

		width = 40
		height = 60
		self.image = pygame.Surface([width, height])
		self.image.fill(RED)
	def draw_player(self):
		pygame.draw.rect(self.x,self.y,self.width,self.height)
		
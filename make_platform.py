import pygame

class platform(pygame.sprite.Sprite):
	def __init__(self, color, width, height, x, yscreen):
		# Call the parent class (Sprite) constructor
		super().__init__()
		
		#Creates image
		# Makes Blue image
		'''self.image = pygame.image.load("platform.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = screen.center'''
		self.rect = pygame.rect(x,y,width,height)
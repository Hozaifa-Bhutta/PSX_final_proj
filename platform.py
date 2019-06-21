import pygame

lass platform(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		# Call the parent class (Sprite) constructor
		super().__init__()

		#Creates image
		self.image = pygame.Surface([width,height])
		# Makes Blue image
		self.image.fill((0,200,0))
        self.image.set_colorkey(WHITE)

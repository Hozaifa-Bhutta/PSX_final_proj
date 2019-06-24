import pygame

class platform(pygame.sprite.Sprite):
	def __init__(self, color, width, height, x, y,screen):
		# Call the parent class (Sprite) constructor
		super().__init__()
		
		#Creates image
		# Makes Blue image
		'''self.image = pygame.image.load("platform.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = screen.center'''
		self.color = color
		self.screen = screen
		self.height = height
		self.x = x
		self.y = y
		self.width = width
		self.rect = pygame.Rect(x,y,width,height)
	def draw_wall(self):	
		pygame.draw.rect(self.screen,self.color,self.rect)

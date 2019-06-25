import pygame
class player(pygame.sprite.Sprite):
	def __init__(self,x,y,screen,platforms):

		super().__init__()
		
		Green = (0, 255, 0)
		self.platforms = platforms
		self.color = Green
		self.width = 40
		self.height = 60
		self.x = x
		self.y = y
		self.screen = screen
		self.rect = pygame.Rect(self.x,self.y,40,60)
		self.speed = 1
		self.velocity = 1
		self.jumping = False
	def draw_player(self):
		pygame.draw.rect(self.screen,self.color, self.rect)
	
	def gravity(self):
		if self.rect.y < 500:
			self.rect.y += self.velocity
			self.velocity += 0.05
		else:
			self.velocity = 1

	def jump(self):
		self.rect.y -= 1

	def go_left(self):
		self.rect.x += -6

	def go_right(self):
		self.rect.x += 6

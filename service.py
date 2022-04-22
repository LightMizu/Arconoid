
import pygame
global screen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
screen = None
class init():
	def __init__(self,scree):
		global screen
		screen = scree
		
def retangle(rect,color):
	pygame.draw.rect(screen,color,rect)
def cirсle(x,y):
	pygame.draw.circle(screen,WHITE,(x,y),4)
class wall():
	x,y =0,0
	rect = None
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect = pygame.Rect(self.x,self.y,10,10)
	def draw(self):
		pygame.draw.rect(screen,WHITE,self.rect)
class ball():
	x,y = 0,0
	rect = None
	vector = (0.5,-1)
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect = pygame.Rect(self.x,self.y,8,8)
	def move(self):
		self.x += self.vector[0]
		self.y += self.vector[1]
		self.rect = pygame.Rect(self.x-4,self.y-4,8,8)
	def check_b(self, blocksc):
		blocks = blocksc.copy()
		for block in blocks:
			wx = block.rect.x
			wy = block.rect.y
			bx = self.rect.x
			by = self.rect.y
			if pygame.Rect(wx+9,wy,1,10).colliderect(pygame.Rect(bx,by,1,8)):
				self.vector = (0 - self.vector[0],self.vector[1])
				blocksc.remove(block)

			if pygame.Rect(wx,wy,1,10).colliderect(pygame.Rect(bx + 7,by,1,8)):
				self.vector = (0 - self.vector[0],self.vector[1])
				blocksc.remove(block)
			if pygame.Rect(wx,wy,10,1).colliderect(pygame.Rect(bx,by + 7,8,1)):
				self.vector = (self.vector[0],0 - self.vector[1])
				blocksc.remove(block)

			if pygame.Rect(wx,wy + 9,10,1).colliderect(pygame.Rect(bx,by,8,1)):
				self.vector = (self.vector[0],0 - self.vector[1])
				blocksc.remove(block)
		return blocksc
				
	def check_w(self,blocks):
		for block in blocks:
			wx = block.rect.x
			wy = block.rect.y
			bx = self.rect.x
			by = self.rect.y
			if pygame.Rect(wx+9,wy,1,10).colliderect(pygame.Rect(bx,by,1,8)):
				self.vector = (0 - self.vector[0],self.vector[1])

			if pygame.Rect(wx,wy,1,10).colliderect(pygame.Rect(bx + 7,by,1,8)):
				self.vector = (0 - self.vector[0],self.vector[1])

			if pygame.Rect(wx,wy,10,1).colliderect(pygame.Rect(bx,by + 7,8,1)):
				self.vector = (self.vector[0],0 - self.vector[1])

			if pygame.Rect(wx,wy + 9,10,1).colliderect(pygame.Rect(bx,by,8,1)):
				self.vector = (self.vector[0],0 - self.vector[1])

	def reverse(self):
		self.vector = (self.vector[0],0-self.vector[1])
	def draw(self):
		cirсle(self.x,self.y)
		
class Block():
	x,y =0,0
	rect = None
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect_obv = pygame.Rect(self.x,self.y,10,10)
		self.rect = pygame.Rect(self.x-1,self.y-1,8,8)
	def draw(self):
		pygame.draw.rect(screen,BLACK,self.rect_obv)
		pygame.draw.rect(screen,GREEN,self.rect)
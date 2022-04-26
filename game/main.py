import os
#from service import *
import pygame
import colorama
from colorama import Fore, Back, Style
os.system('cls')
colorama.init()

def retangle(rect,color):
	pygame.draw.rect(screen,color,rect)
def cirсle(x,y):
	pygame.draw.circle(screen,WHITE,(x,y),4)

class platform():
	x = 0
	y = 0
	rect = None
	def __init__(self,x,y) -> None:
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x-30,y-2,60,4)
	def draw(self):
		retangle(self.rect,(255, 255, 255))
	def move(self,pos):
		x = pos[0]
		y = self.y
		self.rect = pygame.Rect(x-30,y-2,60,4)

class wall():
	x,y =0,0
	rect = None
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect = pygame.Rect((self.x,self.y),(10,10))
	def draw(self):
		pygame.draw.rect(screen,WHITE,self.rect)
class ball():
	x,y = 0,0
	rect = None
	vector = (1,-1)
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
			ww = block.rect.width
			wh = block.rect.height
			bx = self.rect.x
			by = self.rect.y
			if pygame.Rect(wx+ww-1,wy,1,wh).colliderect(pygame.Rect(bx,by,1,8)):
				self.vector = (0 - self.vector[0],self.vector[1])
				blocksc.remove(block)

			if pygame.Rect(wx,wy,1,wh).colliderect(pygame.Rect(bx + 7,by,1,8)):
				self.vector = (0 - self.vector[0],self.vector[1])
				blocksc.remove(block)
			if pygame.Rect(wx,wy,ww,1).colliderect(pygame.Rect(bx,by + 7,8,1)):
				self.vector = (self.vector[0],0 - self.vector[1])
				blocksc.remove(block)

			if pygame.Rect(wx,wy + wh-1,ww,1).colliderect(pygame.Rect(bx,by,8,1)):
				self.vector = (self.vector[0],0 - self.vector[1])
				blocksc.remove(block)

		return blocksc
				
	def check_w(self,blocks):
		bx = self.rect.x
		by = self.rect.y
		for block in blocks:
			wx = block.rect.x
			wy = block.rect.y
			ww = block.rect.width
			wh = block.rect.height

			if pygame.Rect(wx+ww-1,wy,1,wh).colliderect(pygame.Rect(bx,by,1,8)) or pygame.Rect(wx,wy,1,wh).colliderect(pygame.Rect(bx + 7,by,1,8)):
				self.vector = (0 - self.vector[0],self.vector[1])
			
			if pygame.Rect(wx,wy,ww,1).colliderect(pygame.Rect(bx,by + 7,8,1)) or pygame.Rect(wx,wy + wh-1,ww,1).colliderect(pygame.Rect(bx,by,8,1)):
				self.vector = (self.vector[0],0 - self.vector[1])
		
		if pygame.Rect(500,0,1,500).colliderect(pygame.Rect(bx + 7,by,1,8)) or pygame.Rect(0,0,1,500).colliderect(pygame.Rect(bx,by,1,8)):
				self.vector = (0 - self.vector[0],self.vector[1])

		if pygame.Rect(0,0,500,1).colliderect(pygame.Rect(bx,by,8,1)):
			self.vector = (self.vector[0],0 - self.vector[1])
		if pygame.Rect(0,500,500,1).colliderect(pygame.Rect(bx,by + 7,8,1)):
			pygame.quit()



	def reverse(self):
		self.vector = (self.vector[0],0-self.vector[1])
	def draw(self):
		cirсle(self.x,self.y)
		
class block():
	x,y =0,0
	rect = None
	rect_obv = None
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect = pygame.Rect(self.x,self.y,10,10)
		self.rect_obv = pygame.Rect(self.x,self.y,9,9)
	def draw(self):
		pygame.draw.rect(screen,BLACK,self.rect_obv)
		pygame.draw.rect(screen,GREEN,self.rect)

WIDTH = 500
HEIGHT = 500
FPS = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

running = True

b = ball(250,350)
p = platform(250,360)
#init(screen)
try:
	os.mkdir('save')
except OSError:
	pass
print(Fore.GREEN + 'Выберите карту вписав её индекс или полное название(для выхода введите 0):' + Fore.RESET)
ls = os.listdir('save/')

name = ''
for i,d in enumerate(ls):
	if d[-3:] == 'map':
		print(f'{Fore.CYAN}- {Fore.YELLOW}{i+1} | {d[:-4]}{Fore.RESET}')
runn = True
while runn:
	print(Fore.MAGENTA,end='- ')
	s = input()
	if s == '0':
		runn =False
		running = False
		continue
	if s.isdigit():
		try:
			y = ls[int(s)-1]
		except IndexError:
			print(Fore.RED + 'Такой карты нету в списке попробуйте ещё раз')
		else:
			name = f'save\{ls[int(s)-1]}'
			runn = False
	else:
		if s+'.map' in ls:
			j = ls.index(s+'.map')
			name = f'save\{ls[j]}'
			runn = False
if running:
	with open(name,'r') as f:
		lines = f.readlines()
	blocks = []
	walls = []
	for i in lines:
		k = i.strip().split()
		if k[0] == 'W':
			walls.append(wall(int(k[1]),int(k[2])))
		elif k[0] == 'B':
			blocks.append(block(int(k[1]),int(k[2])))
	r = True
	os.system('cls')
	print(Fore.GREEN + 'Загружено!')

while running:
	clock.tick(FPS)
	run = True
	for i in pygame.event.get():
		if i.type == pygame.MOUSEBUTTONDOWN:
			run = False
		if i.type == pygame.QUIT:
			running = False
	screen.fill(BLACK)
	for w in walls:
		w.draw()
	for bl in blocks:
		bl.draw()
	for i in range(0,500,10):
		pygame.draw.line(screen,(0,0,0),(0,i),(500,i))
		pygame.draw.line(screen,(0,0,0),(i,0),(i,500))
	b.draw()
	p.draw()
	pygame.display.flip()
	while r:
		for i in pygame.event.get():
			if i.type == pygame.MOUSEBUTTONDOWN:
				r = False
	pos = pygame.mouse.get_pos()
	b.check_b(blocks)
	b.check_w(walls + [p])
	p.move(pos)
	b.move()
pygame.quit()
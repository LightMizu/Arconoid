import os
import pygame
import colorama
from colorama import Fore, Back, Style
os.system('cls')
try:
	os.mkdir('save')
except OSError:
	...
os.chdir('save')
print(os.getcwd())
colorama.init()

WIDTH = 500
HEIGHT = 500
FPS = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Constructor")
clock = pygame.time.Clock()

running = True

blocks = []
walls = []

while running:
	clock.tick(FPS)
	run = True
	for i in pygame.event.get():
		if i.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			pos = (pos[0]//10*10,pos[1]//10*10)

			if i.button == 1:
				if pos in walls:
					walls.remove(pos)
				else:
					walls.append(pos)
				if pos in blocks:
					blocks.remove(pos)
			if i.button == 3:
				if pos in blocks:
					blocks.remove(pos)
				else:
					blocks.append(pos)
				if pos in walls:
					walls.remove(pos)
		if i.type == pygame.QUIT:
			running = False
	screen.fill(BLACK)
	for i in range(0,500,10):
		pygame.draw.line(screen,(100,100,100),(0,i),(500,i))
		pygame.draw.line(screen,(100,100,100),(i,0),(i,500))
	for wall in walls:
		pygame.draw.rect(screen,WHITE,pygame.Rect(wall[0]+1,wall[1]+1,9,9))
	for block in blocks:
		pygame.draw.rect(screen,GREEN,pygame.Rect(block[0]+1,block[1]+1,9,9))
	pygame.display.flip()
pygame.quit()
print(Fore.YELLOW + 'Введите название карты (для отмены сохранения введите 0):' + Fore.MAGENTA)
n = input()
if n != '0':
	with open(f'{n}.map','w') as f:
		for i in walls:
			print(f'W {i[0]} {i[1]}',file=f)
		for i in blocks:
			print(f'B {i[0]} {i[1]}',file=f)
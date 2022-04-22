from os import system
from tabnanny import check
import pygame
from service import *
system('cls')


WIDTH = 500
HEIGHT = 500
FPS = 240

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
init(screen)
running = True
walls = []
blocks = []
b = ball(265,305)
while running:
	clock.tick(FPS)
	run = True
	for i in pygame.event.get():
		if i.type == pygame.MOUSEBUTTONDOWN:
			run = False
		if i.type == pygame.QUIT:
			running = False
	screen.fill(BLACK)
	plat = [wall(259,360),wall(249,360),wall(239,360)]
	for bl in plat:
		bl.draw()
	for w in walls:
		w.draw()
	for bl in blocks:
		bl.draw()
	b.move()
	b.draw()
	b.check_w(walls)
	b.check_b(blocks)
	
	pygame.display.flip()

pygame.quit()
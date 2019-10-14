import pygame
import random

clock = pygame.time.Clock()

#Экран
size = width, height = 400, 300
screen = pygame.display.set_mode(size)

#Константы
RADIUS = 10
V = 100
FPS = 60
BOT = height - RADIUS

#Списки для координат и скоростей
circle = []
speed = []
colors = []

#Запускаем окно
running = True
while running:
	for event in pygame.event.get():
		#Выход
		if event.type == pygame.QUIT:
			running = False
		#Сохраняем координаты нажатия мыши и генерируем цвет
		if event.type == pygame.MOUSEBUTTONUP:
			x, y = event.pos
			color = [random.randrange(1, 255) for c in range(3)]
			
			circle.append(x)
			speed.append(y)
			colors.append(color)
	
	#Чистка экрана от шаров предыдущего шага
	screen.fill((0, 0, 0))

	#Цикл для отрисовки шаров и изменений их положений, т.е падение
	for i in range(len(circle)):
		speed[i] += V/FPS
		if speed[i] < BOT:
			pygame.draw.circle(screen, colors[i], (circle[i], int(speed[i])), RADIUS)
		else:
			pygame.draw.circle(screen, colors[i], (circle[i], BOT), RADIUS)
	
	#Частота обновления экрана при падении шара
	clock.tick(FPS)
	#Обновление экрана
	pygame.display.flip()

pygame.quit()
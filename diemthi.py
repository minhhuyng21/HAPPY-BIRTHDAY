import pygame

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
BLUE = (255, 165, 0)
CIRCLE_CENTER = [width // 2, height // 2]
ball_pos = [width // 2, height // 2 - 120]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    pygame.draw.circle(screen,BLUE,CIRCLE_CENTER,150,2)
    pygame.draw.circle(screen, (0,0,255), (ball_pos[0],ball_pos[1]), 5)
    pygame.display.flip()
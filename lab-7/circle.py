import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - 3 >= 25: y -= 3
        if pressed[pygame.K_DOWN] and y + 3 <= 275: y += 3
        if pressed[pygame.K_LEFT] and x - 3 >= 25: x -= 3
        if pressed[pygame.K_RIGHT] and x + 3 <= 375: x += 3
        
        screen.fill('white')
        pygame.draw.circle(screen, 'red', (x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)
import pygame, sys, time, random

green = (0, 255, 0)
black = (0,0,0)
red = (255, 0, 0)

snake = [[50, 50], [55, 50], [60, 50], [65, 50]]
food = []


pygame.init()

screen = pygame.display.set_mode((500, 400))

screen.fill(black)
for i in range(len(snake)):
    block = pygame.draw.rect(screen, green, (snake[i][0], snake[i][1], 5, 5))

font = pygame.font.SysFont(None, 18)



while True:
    time.sleep(0.01)
    screen.fill(black)
    for i in range(len(snake)):
        block = pygame.draw.rect(screen, green, (snake[i][0], snake[i][1], 5, 5))

    if len(food) != 1:
        x = random.randrange(5, 395, 5)
        y = random.randrange(5, 395, 5)
        food.append([y, x])
    spawn = pygame.draw.rect(screen, red, (food[0][0], food[0][1], 5, 5))
    if snake[len(snake)-1][0] in food[0] and snake[len(snake)-1][1] in food[0]:
        snake.append([snake[len(snake)-1][0] +5, snake[len(snake)-1][1] +5])
        food.pop(0)
    pygame.display.update()
    pygame.key.set_repeat(1, 12)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_DOWN:
                snake.append([snake[len(snake) -1][0], snake[len(snake) -1][1] +5])
                snake.pop(0)
            elif events.key == pygame.K_RIGHT:
                snake.append([snake[len(snake) -1][0] +5, snake[len(snake) -1][1]])
                snake.pop(0)
            elif events.key == pygame.K_LEFT:
                snake.append([snake[len(snake) -1][0] -5, snake[len(snake) -1][1]])
                snake.pop(0)
            elif events.key == pygame.K_UP:
                snake.append([snake[len(snake) -1][0], snake[len(snake) -1][1] -5])
                snake.pop(0)

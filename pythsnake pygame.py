import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake settings
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color, x, y):
    mesg = font.render(msg, True, color)
    win.blit(mesg, [x, y])

def game_loop():
    game_over = False
    game_close = False
    
    x, y = width // 2, height // 2
    x_change, y_change = 0, 0
    
    snake = []
    length_of_snake = 1
    
    food_x = random.randrange(0, width - snake_block, snake_block)
    food_y = random.randrange(0, height - snake_block, snake_block)
    
    while not game_over:
        while game_close:
            win.fill(black)
            message("Game Over! Press C to Play Again or Q to Quit", red, 50, height // 2)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block
        
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        win.fill(black)
        pygame.draw.rect(win, green, [food_x, food_y, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)
        
        if len(snake) > length_of_snake:
            del snake[0]
        
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True
        
        for segment in snake:
            pygame.draw.rect(win, blue, [segment[0], segment[1], snake_block, snake_block])
        
        message("Score: " + str(length_of_snake - 1), white, 10, 10)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - snake_block, snake_block)
            food_y = random.randrange(0, height - snake_block, snake_block)
            length_of_snake += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

# Run game
game_loop()

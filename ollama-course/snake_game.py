import pygame
import sys
import random

# Game Variables
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'
        self.food = self.generate_food()

    def generate_food(self):
        return (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

    def draw(self):
        self.screen.fill(BLACK)
        for pos in self.snake:
            pygame.draw.rect(self.screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.screen, RED, pygame.Rect(self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'DOWN':
                    self.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.direction != 'UP':
                    self.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                    self.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                    self.direction = 'RIGHT'

        head = self.snake[-1]
        if self.direction == 'UP':
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + BLOCK_SIZE)
        elif self.direction == 'LEFT':
            new_head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == 'RIGHT':
            new_head = (head[0] + BLOCK_SIZE, head[1])

        self.snake.append(new_head)

        if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in self.snake[:-1]):
            self.reset()

        if new_head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

        self.draw()

    def run(self):
        while True:
            self.update()
            self.clock.tick(SPEED)

# if __name__ == "__main__":
#     game = SnakeGame()
#     game.run()
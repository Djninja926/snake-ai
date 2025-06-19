import pygame, sys, random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            # X, Y Positions
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size

            # Creating the Rectangle
            body_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # Draw the Rectangle
            pygame.draw.rect(screen, pygame.Color('green'), body_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy



class Fruit:
    # Create X, Y position
    def __init__(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.pos = Vector2(self.x, self.y)

    # Draw a Square
    def draw_fruit(self):
        # X, Y Positions
        x_pos = self.pos.x * cell_size
        y_pos = self.pos.y * cell_size

        # Creating the Rectangle
        fruit_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        
        # Draw the Rectange
        pygame.draw.rect(screen, (255, 0, 0), fruit_rect)


pygame.init()
pygame.display.set_caption('Snake')

cell_size = 40
cell_num = 20


screen = pygame.display.set_mode((cell_size * cell_num, cell_size * cell_num))
clock = pygame.time.Clock()

fruit = Fruit() 
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)



    # Draw all elements
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)


# Initialize game parameters
# BLOCK_SIZE = 20
# SPEED = 40

# class Direction(Enum):
#     RIGHT = 0
#     LEFT = 1
#     UP = 2
#     DOWN = 3

# Point = namedtuple('Point', 'x, y')

# class SnakeGameAI:
#     def __init__(self, w = 640, h = 480):
#         self.w = w
#         self.h = h
#         self.snake = [Point(self.w/2, self.h/2)]
#         self.direction = Direction.RIGHT
#         self.food = None
#         self._place_food()
#         self.score = 0

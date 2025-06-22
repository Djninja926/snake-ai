import pygame, sys, random
from pygame.math import Vector2

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # Repoistion the Fruit
            self.fruit.randomize()
            # Add a block to the Fruit
            self.snake.add_block()

    def check_fail(self):
        # Check if Snake hits a Wall
        if (not 0 <= self.snake.body[0].x < cell_num) or (not 0 <= self.snake.body[0].y < cell_num):
            self.game_over()
        # Check if Snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    
    def game_over(self):
        pygame.quit()
        sys.exit()

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def add_block(self):
        self.new_block = True

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
        if self.new_block == True:
            body_copy = self.body[:]
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy
        self.new_block = False

class Fruit:
    # Create X, Y position
    def __init__(self):
        self.randomize()

    def randomize(self):
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

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 60)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)



    # Draw all elements
    screen.fill((175, 215, 70))
    main_game.draw_elements()
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

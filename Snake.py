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
            print("Snake hits a Wall")
            self.game_over()
        # Check if Snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                print("Snake Body")
                self.game_over()

    
    def game_over(self):
        pygame.quit()
        sys.exit()

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        # Sound
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def add_block(self):
        self.new_block = True

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down
        else:
            self.head = self.head_right
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down
        else:
            self.tail = self.tail_right

    def update_body_graphics(self):
        for index, block in enumerate(self.body[1:-1]):
            x_pos = int (block.x * cell_size)
            y_pos = int (block.y * cell_size)
            body_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                screen.blit(self.body_vertical, body_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail_up, body_rect)
            else:
                screen.blit(self.body_vertical, body_rect)
            

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        self.update_body_graphics()
        for index, block in enumerate(self.body):
            # X, Y Positions
            x_pos = int (block.x * cell_size)
            y_pos = int (block.y * cell_size)

            # Creating the Rectangle
            body_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # What direction the Snake is Facing
            if index == 0:
                screen.blit(self.head_up, body_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail_up, body_rect)
            else:
                screen.blit(self.body_vertical, body_rect)

            # # Draw the Rectangle
            # pygame.draw.rect(screen, pygame.Color('green'), body_rect)
            


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
        fruit_rect = pygame.Rect(int(x_pos), int(y_pos), cell_size, cell_size)
        
        # Draw the Rectange
        # pygame.draw.rect(screen, (255, 0, 0), fruit_rect)
        screen.blit(apple, fruit_rect)

pygame.init()
pygame.display.set_caption('Snake')

cell_size = 40
cell_num = 20

screen = pygame.display.set_mode((cell_size * cell_num, cell_size * cell_num))
clock = pygame.time.Clock()

apple = pygame.image.load('Graphics/apple.png').convert_alpha()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 60)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exit")
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

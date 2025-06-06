import pygame
from enum import Enum
from collections import namedtuple

# Initialize game parameters
BLOCK_SIZE = 20
SPEED = 40

class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

Point = namedtuple('Point', 'x, y')

class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.snake = [Point(self.w/2, self.h/2)]
        self.direction = Direction.RIGHT
        self.food = None
        self._place_food()
        self.score = 0

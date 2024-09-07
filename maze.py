import pygame
import random

class Maze:
    def __init__(self):
        self.block_size = 100
        self.grid = []

    def generate(self, win_size):
        wnd_width, wnd_height = win_size
        for x in range(300, wnd_width - 299, self.block_size):
            for y in range(0, wnd_height + 1, self.block_size):
                if random.choice([True, False, False]):
                    self.grid.append(pygame.Rect(x, y, self.block_size, self.block_size))

    def draw(self, scr):
        for block in self.grid:
            pygame.draw.rect(scr, (0, 0, 0), block)
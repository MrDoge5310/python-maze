import pygame
import random


class Maze:
    def __init__(self, width=1180, height=750, block_size=40):
        self.block_size = block_size
        self.grid_width = width // block_size
        self.grid_height = height // block_size
        self.visited = [[False for _ in range(self.grid_height)] for _ in range(self.grid_width)]
        self.stack = []
        self.grid = []  # Список для хранения блоков как объектов Rect

    def generate(self):
        # Начинаем с левого верхнего угла
        start_x, start_y = 0, 0
        self.stack.append((start_x, start_y))
        self.visited[start_x][start_y] = True

        while self.stack:
            x, y = self.stack[-1]
            neighbors = self.get_neighbors(x, y)

            if neighbors:
                next_x, next_y = random.choice(neighbors)
                # Убираем стену и создаём проход
                self.visited[next_x][next_y] = True
                self.stack.append((next_x, next_y))

                # Добавляем блоки в список
                self.add_block(x, y)
                self.add_block((x + next_x) // 2, (y + next_y) // 2)  # Проход между блоками
            else:
                self.stack.pop()

        # Обеспечиваем наличие выхода в правом нижнем углу
        self.ensure_exit()

    def get_neighbors(self, x, y):
        neighbors = []
        if x > 1 and not self.visited[x - 2][y]:
            neighbors.append((x - 2, y))
        if x < self.grid_width - 2 and not self.visited[x + 2][y]:
            neighbors.append((x + 2, y))
        if y > 1 and not self.visited[x][y - 2]:
            neighbors.append((x, y - 2))
        if y < self.grid_height - 2 and not self.visited[x][y + 2]:
            neighbors.append((x, y + 2))
        return neighbors

    def add_block(self, x, y):
        if x in range(self.grid_width - 4):
            if y  in range (self.grid_height - self.block_size * 5, self.grid_height):
                block = pygame.Rect(x * self.block_size + 50, y * self.block_size, self.block_size, self.block_size)
                self.grid.append(block)

    def ensure_exit(self):
        # Правый нижний угол
        exit_x = self.grid_width - 1
        exit_y = self.grid_height - 1

        # Убираем блоки, если они присутствуют в этих ячейках (вход и выход)
        if (exit_x * self.block_size, exit_y * self.block_size) in [(block.x, block.y) for block in self.grid]:
            self.grid = [block for block in self.grid if
                         (block.x, block.y) != (exit_x * self.block_size, exit_y * self.block_size)]

        # Также убираем блок в левом верхнем углу
        if (0, 0) in [(block.x, block.y) for block in self.grid]:
            self.grid = [block for block in self.grid if (block.x, block.y) != (0, 0)]

    def draw(self, scr):


        for block in self.grid:
            # Сдвигаем каждый блок на offset_x и offset_y
            pygame.draw.rect(scr, (0, 0, 0), block)
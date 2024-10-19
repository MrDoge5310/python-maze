import pygame
import random

class Maze:
    def __init__(self, width=1180, height=800, block_size=70):
        self.block_size = block_size
        self.grid_width = width // block_size
        self.grid_height = height // block_size
        self.visited = [[False for _ in range(self.grid_height)] for _ in range(self.grid_width)]
        self.stack = []
        self.grid = []  # Список для хранения блоков как объектов Rect

    def generate(self):
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
        # Создаём объект Rect для блока и добавляем его в список
        block = pygame.Rect(x * self.block_size + 50, y * self.block_size, self.block_size, self.block_size)
        self.grid.append(block)

    def draw(self, scr):
        win_width, win_height = scr.get_size()
        # Вычисляем отступы для центрирования лабиринта
        offset_x = (win_width - (self.grid_width * self.block_size)) // 2
        offset_y = (win_height - (self.grid_height * self.block_size)) // 2

        for block in self.grid:

            # Сдвигаем каждый блок на offset_x и offset_y
            # block = block.move(offset_x, offset_y)
            pygame.draw.rect(scr, (0, 0, 0), block)
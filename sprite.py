import pygame


class Sprite:
    def __init__(self, image_path, position=(0, 0)):
        self.image = pygame.image.load(image_path)
        width = 100
        height = 100
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def __init__(self, image_path, position=(0, 0)):
        super().__init__(image_path, position)
        self.step = 5

    def checkCollide(self, maze):
        for m in maze:
            if self.rect.colliderect(m):
                return True
            else:
                return False

    def move(self, win_size, maze):
        win_width, win_height = win_size
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.step
            if self.checkCollide(maze):
                self.rect.x += self.step
        elif keys[pygame.K_RIGHT] and self.rect.right <= win_width:
            self.rect.x += self.step
            if self.checkCollide(maze):
                self.rect.x -= self.step
        elif keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.step
            if self.checkCollide(maze):
                self.rect.y += self.step
        elif keys[pygame.K_DOWN] and self.rect.bottom < win_height:
            self.rect.y += self.step
            if self.checkCollide(maze):
                print('down')
                self.rect.y -= self.step


class Target(Sprite):
    def __init__(self, image_path, position=(0, 0)):
        super().__init__(image_path, position)

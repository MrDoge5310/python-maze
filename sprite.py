import pygame


class Sprite:
    def __init__(self, image_path, position=(0, 0)):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def __init__(self, image_path, position=(0, 0)):
        super().__init__(image_path, position)
        self.step = 5

    def move(self, win_width, win_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.step
        if keys[pygame.K_RIGHT] and self.rect.x < win_width - 64:
            self.rect.x += self.step
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.step
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 64:
            self.rect.y += self.step


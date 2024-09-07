import pygame
from sprite import Player, Target
from maze import Maze


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

player = Player('kapibara.png')
target = Target('target.png')
maze = Maze()
maze.generate(screen.get_size())



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    player.draw(screen)
    target.draw(screen)
    maze.draw(screen)
    player.move(screen.get_size(), maze.grid)  # update player's position based on keyboard input'

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()

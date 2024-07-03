import sys, pygame
import Player
pygame.init()

size = width, height = 1200, 1200
screen = pygame.display.set_mode(size)
player = Player()

while True:
  for e in pygame.event.get():
    if e.type == pygame.QUIT: sys.exit()
    player.handleEvent(e)
  
  screen.fill("green")
  pygame.display.flip()
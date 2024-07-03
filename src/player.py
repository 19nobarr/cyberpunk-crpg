import pygame

# player object contains everything that has to do with the player during the game
# if the player has a character
# what position the player is in 
# any player inputs 
  # accessing the settings
  # movement
  # actions
    # shooting
  # clicking through menus

class Player: 

  def __init__(self):
    self._pos = (0,0)

  def handleEvent(self, event: pygame.event.Event.type):

    if event == pygame.KEYUP:
      print("Keyed Up!")
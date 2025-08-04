from stateMan.stateMan import StateManager
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Veilbreaker")

manager = StateManager(screen)
manager.run()

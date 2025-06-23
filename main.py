import pygame
import player

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Veilbreaker")
clock = pygame.time.Clock()
running = True
Player = player.Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    Player.show(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

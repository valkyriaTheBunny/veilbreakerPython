from player import Player
from world import World
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Veilbreaker")
clock = pygame.time.Clock()
running = True
player = Player()
world = World()

world.genRoom()
initPos = world.sPos()
player.setPos(initPos[0], initPos[1])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            pos = player.getPos()

            if key[pygame.K_w] or key[pygame.K_UP]:
                pos[1] -= 1
            if key[pygame.K_s] or key[pygame.K_DOWN]:
                pos[1] += 1
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                pos[0] -= 1
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                pos[0] += 1

            if world.checkPos(pos[0], pos[1]):
                player.setPos(pos[0], pos[1])
                world.update()

    screen.fill("black")
    world.show(screen)
    player.show(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

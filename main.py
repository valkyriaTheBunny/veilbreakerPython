from characters.player import Player
from world.world import World
from equipment.weapons import Weapon
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Veilbreaker")
clock = pygame.time.Clock()
running = True
player = Player()
world = World()

world.genRoom(1)
initPos = world.sPos()
player.setPos(initPos[0], initPos[1])
world.getGrid()[initPos[0]][initPos[1]] = "player"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
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

            if world.checkPos(pos[0], pos[1], "occupied"):
                mon = world.getGrid([pos[0]], [pos[1]])
                player.attack(mon)

            if world.checkPos(pos[0], pos[1]):
                player.setPos(pos[0], pos[1])
                world.getGrid()[pos[0]][pos[1]] = "player"
                #world.update(player)

    screen.fill("black")
    world.show(screen)
    player.show(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

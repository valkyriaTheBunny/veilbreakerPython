from characters.player import Player
from world.map import World
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Veilbreaker")
clock = pygame.time.Clock()
running = True
player = Player()
world = World()

world.genRooms()
initPos = world.sPos()
player.setPos(initPos[0], initPos[1])
world.updateGrid(initPos[0], initPos[1], "player")
dt = 0

while running:
    dt += clock.get_time()
    world.update(player, dt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            pos = player.getPos()
            print(pos)

            if key[pygame.K_w] or key[pygame.K_UP]:
                print("up")
                pos[1] -= 1
            if key[pygame.K_s] or key[pygame.K_DOWN]:
                print("down")
                pos[1] += 1
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                print("left")
                pos[0] -= 1
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                print("right")
                pos[0] += 1

            print(pos)
            print(world.checkPos(pos[0], pos[1], caller="main"))
            if world.checkPos(pos[0], pos[1], "occupied", "main"):
                print("ah! a monster")
                mon = world.isOccupied(pos[0], pos[1], player.getAtkVal())
                if mon:
                    player.attack(mon)
                #the second if here is to make sure that a dead monster does not try to attack
                if mon:
                    mon.attack(player)
            if world.checkPos(pos[0], pos[1], caller="main"):
                print("safe")
                oPos = player.getPos()
                world.updateGrid(oPos[0], oPos[1], "floor")
                player.setPos(pos[0], pos[1])
                world.updateGrid(pos[0], pos[1], "player")

    screen.fill("black") #probably don't really need this line
    world.show(screen)
    player.show(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

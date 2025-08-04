from characters.player import Player
from world.map import World
import pygame

class StateManager:
    def __init__(self, screen):
        self.__state = "Main"
        self.__screen = screen

    def run(self):
        if self.__state == "Start":
            pass
        elif self.__state == "Main":
            clock = pygame.time.Clock()
            running = True
            player = Player()
            world = World()

            world.genRooms()
            initPos = world.sPos()
            player.setPos(initPos[0], initPos[1])
            world.updateGrid(initPos[0], initPos[1], "player")
            dt = 0
            dir = None

            while running:
                dt += clock.get_time()
                world.update(player, dt)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        pos = player.getPos()

                        if key[pygame.K_w] or key[pygame.K_UP]:
                            pos[1] -= 1
                            dir = "up"
                        if key[pygame.K_s] or key[pygame.K_DOWN]:
                            pos[1] += 1
                            dir = "down"
                        if key[pygame.K_a] or key[pygame.K_LEFT]:
                            pos[0] -= 1
                            dir = "left"
                        if key[pygame.K_d] or key[pygame.K_RIGHT]:
                            pos[0] += 1
                            dir = "right"

                        if world.checkPos(pos[0], pos[1], "occupied"):
                            mon = world.isOccupied(pos[0], pos[1], player.getAtkVal())
                            if mon:
                                player.attack(mon)
                            #the second if here is to make sure that a dead monster does not try to attack
                            if mon:
                                mon.attack(player)
                        if world.checkPos(pos[0], pos[1]):
                            oPos = player.getPos()
                            world.updateGrid(oPos[0], oPos[1], "floor")
                            player.setPos(pos[0], pos[1])
                            world.updateGrid(pos[0], pos[1], "player")
                        if world.checkPos(pos[0], pos[1], "door"):
                            world.isDoor(pos[0], pos[1], dir)
                            nPos = world.sPos()
                            player.setPos(nPos[0], nPos[1])
                        if world.checkPos(pos[0], pos[1], "fount"):
                            world.runFount(player)

                world.show(self.__screen)
                player.show(self.__screen)
                pygame.display.flip()
                clock.tick(60)

            pygame.quit()

from characters.player import Player
from world.map import World
import pygame, sys

class StateManager:
    def __init__(self):
        self.__state = "Main"
        self.__runtime = 0

    def run(self):
        while True:
            if self.__state == "Start":
                pass
            elif self.__state == "Main":
                self.__main_scene()
            elif self.__state == "Score":
                self.__score_scene()

    def __main_scene(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((1200, 700))
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
        runtime = 0
        dir = None

        while running:
            runtime += dt
            world.update(player, runtime)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
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

                if world.empty():
                    self.__state = "Score"
                    self.__runtime = runtime
                    running = False

                if player.health <= 0:
                    running = False
                    pygame.quit()
                    sys.exit()

            world.show(self.__screen)
            player.show(self.__screen)
            pygame.display.flip()
            dt = clock.tick(60)

    def __score_scene(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Veilbreaker")
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.__screen.fill("black")
            font = pygame.font.Font('assets/font/JMH Typewriter.ttf')

            hours = self.__runtime // 3600000
            minutes = (self.__runtime % 3600000) // 60000
            seconds = (self.__runtime % 60000) // 1000
            milli = self.__runtime % 1000

            runText = font.render(f'Congradulations! Your runtime was: {hours}:{minutes}:{seconds}.{milli}', False, "white")
            runTextRect = runText.get_rect()
            runTextRect.center = (600, 350)

            self.__screen.blit(runText, runTextRect)

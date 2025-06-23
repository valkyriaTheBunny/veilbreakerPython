import pygame
import player
import world

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Veilbreaker")
clock = pygame.time.Clock()
running = True
Player = player.Player()
World = world.World()

World.genRoom()
initPos = World.sPos()
Player.setPos(initPos[0], initPos[1])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed

            if key == pygame.K_w or key == pygame.K_UP:
                pass

    screen.fill("black")
    World.show(screen)
    Player.show(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

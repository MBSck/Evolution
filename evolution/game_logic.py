import pygame

from options import OPTIONS


def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((OPTIONS["screen.width"],
                                      OPTIONS["screen.height"]))
    pygame.display.set_caption("Evolution")

    while OPTIONS["running"]:
        # NOTE: Exit behaviour
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                OPTIONS["running"] = False

        # NOTE: Game logic

        # NOTE: Update behaviour
        screen.fill((0, 255, 0))
        pygame.display.update()

    pygame.quit()

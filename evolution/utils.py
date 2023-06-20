import pygame


def draw_grid(screen,
              window_width: int,
              window_height: int,
              grid_width: int,
              grid_height: int):
    """Draws a grid.

    This function is simply for debug purposes.
    """
    for x in range(0, window_width, grid_width):
        for y in range(0, window_height, grid_height):
            rect = pygame.Rect(x, y, grid_width, grid_height)
            pygame.draw.rect(screen, pygame.Color("white"), rect, 1)

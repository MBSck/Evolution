from typing import Tuple, Optional

import numpy as np
import pygame


def calculate_grid_dimensions(window_width: int,
                              window_height: int,
                              cells_per_side: int) -> Tuple[int, int]:
    """Calculates the number of rows and columns of the grid
    from the set resolution dependent on the number of cells.

    Parameters
    ----------
    window_width : int
    window_height : int
    cells_per_side : int

    Returns
    -------
    grid_size : Tuple[int, int]
    """
    return window_width // cells_per_side,\
        window_height // cells_per_side


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

from typing import Tuple, Optional

import numpy as np
import pygame


def next_even_power_of_two(power: int, mode: Optional[str] = "lower") -> int:
    """Gets the next even power of two.

    Parameters
    ----------
    power : int
    mode : str, optional

    Returns
    -------
    next_power : int
    """
    if mode == "lower":
        next_power = np.floor(np.log2(power))
        return 2**(next_power - 1) if next_power % 2 != 0 else 2**next_power
    next_power = np.ceil(np.log2(power))
    return 2**(next_power + 1) if next_power % 2 != 0 else 2**next_power


def calculate_grid_dimensions(window_width: int,
                              window_height: int,
                              cell_number: int) -> Tuple[int, int]:
    """Calculates the number of rows and columns of the grid
    from the set resolution dependent on the number of cells.

    Parameters
    ----------
    window_width : int
    window_height : int
    cell_number : int

    Returns
    -------
    grid_size : Tuple[int, int]
    """
    half_cell_number = next_even_power_of_two(cell_number) // 2
    return int(window_width / half_cell_number),\
        int(window_height / half_cell_number)


def draw_grid(screen,
              window_width: int,
              window_height: int,
              grid_width: int,
              grid_height: int):
    """Draws the grid.

    Function for Debug purposes.
    """
    for x in range(0, window_width, grid_width):
        for y in range(0, window_height, grid_height):
            rect = pygame.Rect(x, y, grid_width, grid_height)
            pygame.draw.rect(screen, pygame.Color("white"), rect, 1)

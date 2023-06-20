from typing import Tuple

import numpy as np

from utils import calculate_grid_dimensions


# TODO: Fix this grid, make it the correct number
def create_grid(window_width: int,
                window_height: int,
                cells_per_side: int) -> None:
    """Creates the grid cells that can hold entities.

    Parameters
    ----------
    window_width : int
    window_height : int
    cells_per_side : int

    Returns
    -------
    grid : np.ndarray
    """
    return np.zeros(
        calculate_grid_dimensions(window_width, window_height, cell_number)).flatten()


def get_entity_grid_coordinates(entity) -> Tuple:
    ...


def add_entity_to_grid() -> None:
    ...

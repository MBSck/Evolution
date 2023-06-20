from typing import Optional, Tuple

import numpy as np


def calculate_cell_dimensions(window_width: int,
                              window_height: int,
                              cells_per_side: int) -> Tuple:
    """Calculates the dimensions of a cell in x and y.

    Parameters
    ----------
    window_width : int
        The width of the window.
    window_height : int
        The height of the window.
    cells_per_side : int
        The number of cells per side.

    Returns
    -------
    cell_dimensions : tuple
        The dimensions of a cell.
    """
    return window_width // cells_per_side,\
        window_height // cells_per_side


def calculate_grid_dimensions(*args) -> Tuple:
    """Calculates the dimensions of the 2D grid.

    Parameters
    ----------
    window_width : int
        The width of the window.
    window_height : int
        The height of the window.
    cells_per_side : int
        The number of cells per side.

    Returns
    -------
    grid_dimensions : tuple
        The dimensions of the 2D grid.
    """
    return (args[-1], args[-1], *calculate_cell_dimensions(*args))


# TODO: Work in progress, add here the proper adding of entities.
def create_grid(*args, kind: Optional[str] = "random") -> None:
    """Creates the grid cells that can hold entities.

    Parameters
    ----------
    window_width : int
        The width of the window.
    window_height : int
        The height of the window.
    cells_per_side : int
        The number of cells per side.

    Returns
    -------
    grid : numpy.ndarray
    """
    shape = np.zeros(calculate_grid_dimensions(*args)).flatten().shape
    if kind == "random":
        grid = np.random.randint(2, size=shape)
    return grid


def get_2d_grid(grid: np.ndarray, *args) -> np.ndarray:
    """Returns the grid as a 2D numpy array.

    Parameters
    ----------
    grid : numpy.ndarray
        The grid as a 1D numpy array.
    window_width : int
        The width of the window.
    window_height : int
        The height of the window.
    cells_per_side : int
        The number of cells per side.

    Returns
    -------
    reshaped_grid : numpy.ndarray
        The grid as a 2D numpy array.

    Notes
    -----
    This is a convinience function to easier assign indices to the grid.
    """
    return grid.reshape(*calculate_grid_dimensions(*args))


def relate_2d_to_1d_grid_indices(quadrant_number: int,
                                 x_index: int, y_index: int,
                                 grid: np.ndarray, *args):
    """Relates the 2D grid to the 1D grid indices.

    Parameters
    ----------
    quadrant_number : int
        The quadrant number.
    x_index : int
        The x index of the quadrant.
    y_index : int
        The y index of the quadrant.
    window_width : int
        The width of the window.
    window_height : int
        The height of the window.
    cells_per_side : int
        The number of cells per side.

    Returns
    -------
    1D_grid_index : int
        The 1D grid index.
    """
    shape_2d = get_2d_grid(grid, *args).shape
    quadrant_indices = np.unravel_index(quadrant_number, shape_2d[:2])
    indices = (*quadrant_indices, x_index, y_index)
    return np.ravel_multi_index(indices, shape_2d)




def get_entity_grid_coordinates(entity) -> Tuple:
    ...


def add_entity_to_grid() -> None:
    ...


if __name__ == "__main__":
    args = (8, 8, 4)
    grid_1d = create_grid(*args)
    grid_2d = get_2d_grid(grid_1d, *args)
    print(grid_1d)

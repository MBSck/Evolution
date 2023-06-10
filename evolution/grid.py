import numpy as np

from utils import calculate_grid_dimensions


# TODO: Fix this grid, make it the correct number
def create_grid_cells(window_width: int,
                      window_height: int,
                      cell_number: int) -> None:
    """Creates the grid cells that can hold entities."""
    return np.zeros(
        calculate_grid_dimensions(window_width, window_height, cell_number))


def get_entity_grid_coordinates():
    ...


def add_entity_to_grid():
    ...

if __name__ == "__main__":
    test = create_grid_cells(1024, 640, 128)
    breakpoint()

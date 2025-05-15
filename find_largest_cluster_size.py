import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# 2D array:
ROWS = 2  # Must be > 0
COLS = 9  # Must be > 0


class Cell:
    value = 1
    visited = False

    neighbor_up = None
    neighbor_down = None
    neighbor_left = None
    neighbor_right = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def generate_np_array(rows, cols):
    np_array = np.random.randint(0, 2, size=(rows, cols))

    print(np_array)

    sns.heatmap(np_array, cmap="Blues", cbar=False, linewidths=0.5)
    plt.show()

    return np_array


def model_np_array_to_cell_array(np_array):
    rows, cols = np_array.shape

    # Init the Cells
    cells = [
        [None for _ in range(COLS)] for _ in range(ROWS)
    ]

    for x in range(rows):
        for y in range(cols):
            cells[x][y] = Cell(
                value=np_array[x, y],
                visited=False,

                neighbor_up=None,
                neighbor_down=None,
                neighbor_left=None,
                neighbor_right=None
            )

    # Init the Cell's neighbors
    for x in range(rows):
        for y in range(cols):
            cell = cells[x][y]
            cell.neighbor_up = cells[x-1][y] if x-1 >= 0 else None
            cell.neighbor_down = cells[x+1][y] if x+1 < rows else None
            cell.neighbor_left = cells[x][y-1] if y-1 >= 0 else None
            cell.neighbor_right = cells[x][y+1] if y+1 < cols else None

    return cells


def cell_traverse(cell, current_cluster_size):
    # BFS
    if cell is None:
        return current_cluster_size

    if cell.visited:
        return current_cluster_size

    if cell.value == 0:
        return current_cluster_size

    cell.visited = True
    current_cluster_size[0] = current_cluster_size[0] + 1

    # Recursively
    cell_traverse(cell.neighbor_up, current_cluster_size)
    cell_traverse(cell.neighbor_down, current_cluster_size)
    cell_traverse(cell.neighbor_left, current_cluster_size)
    cell_traverse(cell.neighbor_right, current_cluster_size)

    return current_cluster_size


def find_largest_cluster_size():
    np_array = generate_np_array(ROWS, COLS)
    cell_array = model_np_array_to_cell_array(np_array)
    largest_cluster_size = 0

    rows, cols = np_array.shape
    for x in range(rows):
        for y in range(cols):
            cell = cell_array[x][y]
            current_cluster_size = [0]

            if cell.value == 1 and cell.visited == False:
                current_cluster_size = cell_traverse(cell, current_cluster_size)
                largest_cluster_size = max(current_cluster_size[0], largest_cluster_size)

    print(f"The largest cluster's size: {largest_cluster_size}")
    return largest_cluster_size


def main():
    return find_largest_cluster_size()


if __name__ == "__main__":
    main()

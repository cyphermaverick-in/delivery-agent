"""visualization.py
Utilities to draw a grid, obstacles, moving obstacles and a path using matplotlib.
"""
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple

def draw_grid(grid, path=None, start=None, goal=None, title=None, savepath=None):
    arr = np.zeros((grid.rows, grid.cols))
    for r in range(grid.rows):
        for c in range(grid.cols):
            v = grid.cells[r][c]
            if v == 1:
                arr[r,c] = -1
            elif v > 1:
                arr[r,c] = 0.5
            else:
                arr[r,c] = 0
    fig,ax = plt.subplots()
    ax.imshow(arr, cmap='gray', origin='upper')
    if path:
        ys=[p[1] for p in path]
        xs=[p[0] for p in path]
        ax.plot(ys,xs)  # note: swap for row/col
    if start:
        ax.scatter([start[1]],[start[0]], marker='o', label='start')
    if goal:
        ax.scatter([goal[1]],[goal[0]], marker='x', label='goal')
    ax.set_xticks([]); ax.set_yticks([])
    if title: ax.set_title(title)
    if savepath:
        plt.savefig(savepath)
    else:
        plt.show()

"""generate_maps.py
Utility to procedurally generate maps for testing.
"""
import random

def generate(rows, cols, obstacle_prob=0.15, high_cost_prob=0.05):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if random.random() < obstacle_prob:
                row.append(1)  # obstacle
            elif random.random() < high_cost_prob:
                row.append(3)  # higher cost terrain
            else:
                row.append(0)  # free cell
        grid.append(row)
    return grid

def save_map(filename, grid):
    rows, cols = len(grid), len(grid[0])
    with open(filename, 'w') as f:
        f.write(f"{rows} {cols}\n")
        for row in grid:
            f.write(" ".join(map(str, row)) + "\n")

if __name__ == "__main__":
    # Generate medium map
    medium = generate(20, 20)
    save_map("maps/medium.txt", medium)
    print("Saved maps/medium.txt")

    # Generate large map
    large = generate(40, 40)
    save_map("maps/large.txt", large)
    print("Saved maps/large.txt")
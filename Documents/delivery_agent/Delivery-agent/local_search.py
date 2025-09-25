"""local_search.py
Provides a simple simulated annealing style replanner that tries to repair a path when blocked.
This is a proof-of-concept and not state-of-the-art.
"""
import random
import math
from typing import List, Tuple

# Path is list of (r,c) coordinates. We try small modifications to find lower-cost path under constraints.

def path_cost(grid, path):
    return sum(grid.cost(r,c) for r,c in path)

def random_neighbor_path(path, grid):
    # pick an index in path (not endpoints) and attempt to reconnect by short A* between neighbors
    if len(path) < 4:
        return path
    i = random.randint(1, len(path)-2)
    # try to replace segment [i-1 ... i+1] by alternative
    a = path[i-1]; b = path[i+1]
    # naive: try direct neighbor replacement
    candidates = list(grid.neighbors(*a))
    candidates = [c for c in candidates if c!=path[i-1] and c!=path[i] and c!=path[i+1]]
    if not candidates:
        return path
    new_mid = random.choice(candidates)
    new_path = path[:i] + [new_mid] + path[i+1:]
    return new_path

def simulated_annealing_repair(grid, path, iterations=200, start_temp=10.0):
    best = path[:]
    best_cost = path_cost(grid,best)
    cur = best[:]
    cur_cost = best_cost
    for t in range(iterations):
        T = start_temp * (1 - t/iterations)
        cand = random_neighbor_path(cur, grid)
        cand_cost = path_cost(grid,cand)
        if cand_cost < cur_cost or random.random() < math.exp((cur_cost-cand_cost)/max(1e-6,T)):
            cur = cand; cur_cost=cand_cost
            if cur_cost < best_cost:
                best = cur[:]; best_cost = cur_cost
    return best, best_cost

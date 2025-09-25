"""agent.py
CLI to run planners on maps.
"""
import argparse
from grid import load_map_simple
from search import bfs, ucs, astar
from visualization import draw_grid

ALGO_MAP = {
    'bfs': bfs,
    'ucs': ucs,
    'astar': astar,
}

if __name__=='__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--map', required=True)
    p.add_argument('--algo', required=True, choices=ALGO_MAP.keys())
    p.add_argument('--start', default='0,0')
    p.add_argument('--goal', default=None)
    p.add_argument('--visualize', action='store_true')
    p.add_argument('--diagonals', action='store_true')
    args = p.parse_args()

    grid = load_map_simple(args.map)
    s = tuple(map(int,args.start.split(',')))
    if args.goal:
        g = tuple(map(int,args.goal.split(',')))
    else:
        g = (grid.rows-1, grid.cols-1)

    algo = ALGO_MAP[args.algo]
    path, cost, nodes, duration = algo(grid, s, g)
    print(f"Result: path_length={(len(path) if path else 0)} cost={cost} "
          f"nodes_expanded={nodes} time={duration:.4f}s")

    if args.visualize and path:
        draw_grid(grid, path=path, start=s, goal=g, title=f"{args.algo} path")
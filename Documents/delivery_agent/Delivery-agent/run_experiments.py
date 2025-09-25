"""run_experiments.py
Run planners on a set of maps, collect metrics and save JSON/CSV results plus simple plots.
"""
import json
import os
from search import bfs, ucs, astar
from grid import load_map_simple
from visualization import draw_grid

ALGORITHMS = [
    ('bfs', bfs),
    ('ucs', ucs),
    ('astar', astar),
]

# Add all your maps here
MAPS = [
    ('small', 'maps/small.txt'),
    ('medium', 'maps/medium.txt'),
    ('large', 'maps/large.txt'),
]

if __name__ == '__main__':
    results = []
    os.makedirs('results', exist_ok=True)

    for mname, mfile in MAPS:
        grid = load_map_simple(mfile)
        start = (0, 0)
        goal = (grid.rows - 1, grid.cols - 1)

        for aname, algo in ALGORITHMS:
            path, cost, nodes, dur = algo(grid, start, goal)
            results.append({
                'map': mname,
                'algo': aname,
                'path_len': len(path) if path else 0,
                'cost': cost,
                'nodes': nodes,
                'time': dur,
            })
            print(f"{mname} {aname}: cost={cost} nodes={nodes} time={dur:.4f}s")

            # Save visualization for each run
            if path:
                savepath = f"results/{mname}_{aname}.png"
                draw_grid(grid, path=path, start=start, goal=goal,
                          title=f"{mname} {aname}", savepath=savepath)

    # Save summary JSON
    with open('results/summary.json', 'w') as f:
        json.dump(results, f, indent=2)

    print("\nSaved results/summary.json and visualizations in results/")
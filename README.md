# Delivery-agent
🚚🤖 Autonomous Delivery Agent Project Scaffold
## Project structure
```
delivery-agent/
│── README.md
│── requirements.txt
│── main.py
│── environment.py
│── search_algorithms.py
│── local_search.py
│── agent.py
│── utils.py
│── maps/
│    ├── small.txt
│    ├── medium.txt
│    ├── large.txt
│    ├── dynamic.txt
│    ├── dynamic.schedule.json
│── results/
│    ├── results.csv
│    ├── plots.png
│── report/
│    ├── report.pdf
│    ├── figures/
```
## Project overview

This project builds an autonomous delivery agent that navigates a 2D grid city to deliver packages. The agent supports:

* Environment modelling (static obstacles, varying terrain movement cost, moving obstacles)
* Uninformed search: BFS and Uniform-Cost Search (UCS)
* Informed search: A* with admissible heuristics
* Local search replanning: Hill-Climbing with Random Restarts (for dynamic / unpredictable obstacles)
* Experimental comparison across map sizes (small, medium, large) + dynamic map

**Design choices used in this scaffold**

* Movement: **4-connected** (up, down, left, right) — follows assignment default.
* Local search: **Hill-Climbing with Random Restarts** (as requested).
* Language: **Python 3.10+**.
* Dependencies: only `numpy` and `matplotlib` (plus Python standard library).

---

## `requirements.txt`

```
numpy>=1.25
matplotlib>=3.8
```

---

## Map file format (simple grid text)

Each map file is a plain text grid where each cell is an integer or a special symbol. Cells are space-separated. Rows are newline-separated.

Legend (example):

* `.` or `1` : normal traversable cell with movement cost = 1
* `2`, `3`, ... : traversable cell with movement cost = that integer
* `#` : static obstacle (wall) — cannot traverse
* `S` : start cell (agent initial position)
* `G` : goal cell (delivery location)
* `M` : moving obstacle path markers (for dynamic map; see schedule JSON)

**Example small map (5x6):**

```
S 1 1 1 1 G
1 # 2 2 1 1
1 1 1 # 1 1
1 2 1 1 1 1
1 1 1 1 1 1
```

---

## Example maps

### maps/small.txt (6x5)

```
S 1 1 1 1 G
1 # 2 2 1 1
1 1 1 # 1 1
1 2 1 1 1 1
1 1 1 1 1 1
```

### maps/medium.txt (10x8)

```
S 1 1 1 1 1 1 1 1 G
1 # # 2 2 2 # 1 1 1
1 1 1 1 # 1 1 1 1 1
1 2 2 1 1 1 # 2 2 1
1 1 # 1 # 1 1 1 1 1
1 1 1 1 2 2 2 1 # 1
1 # 1 # 1 1 1 1 1 1
1 1 1 1 1 # 1 2 2 1
```

### maps/large.txt (15x12)

```
S 1 1 1 1 1 1 1 1 1 1 1 1 1 G
1 # # 2 2 2 # 1 1 1 1 2 2 1 1
1 1 1 1 # 1 1 1 1 1 1 # 1 1 1
1 2 2 1 1 1 # 2 2 1 1 1 1 1 1
1 1 # 1 # 1 1 1 1 1 # 1 1 1 1
1 1 1 1 2 2 2 1 # 1 1 1 1 2 2
1 # 1 # 1 1 1 1 1 1 1 1 # 1 1
1 1 1 1 1 # 1 2 2 1 1 1 1 1 1
1 2 1 1 1 1 1 1 1 2 2 2 1 # 1
1 1 1 # 1 1 1 1 # 1 1 1 1 1 1
1 1 2 2 2 1 # 1 1 1 2 2 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
```

### maps/dynamic.txt (8x8)

```
S 1 1 1 1 1 1 G
1 # # 1 1 2 1 1
1 1 1 1 # 1 1 1
1 2 2 1 1 1 # 1
1 1 # 1 # 1 1 1
1 M 1 1 2 2 1 1
1 # 1 # 1 1 1 1
1 1 1 1 1 # 1 1
```

### maps/dynamic.schedule.json

```json
{
  "moving_obstacles": [
    {
      "id": "car1",
      "path": [[5,1], [5,2], [5,3], [5,4], [5,5]],
      "repeat": true
    },
    {
      "id": "car2",
      "path": [[2,2], [3,2], [4,2], [5,2], [6,2]],
      "repeat": true
    }
  ]
}
```

Coordinates are in `(row, col)` starting from `(0,0)` top-left.

---

## CLI (examples)

Run A* on medium map:

```bash
python main.py --map maps/medium.txt --algo astar --out results/medium_astar.csv
```

Run UCS on large map:

```bash
python main.py --map maps/large.txt --algo ucs --out results/large_ucs.csv
```

Run hill-climbing replanning on dynamic map (show logs):

```bash
python main.py --map maps/dynamic.txt --algo hill --visualize --log results/dynamic_hill.log
```

Get help:

```bash
python main.py --help
```

---

## Next steps

Maps and schedule are now defined. Next, I will generate **environment.py** which:

* Loads maps and schedule
* Represents grid with costs and obstacles
* Updates positions of moving obstacles (per timestep)
* Provides neighbors and cost lookups

To connect : reshabh.dev@outlook.com

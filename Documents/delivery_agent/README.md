# Autonomous Delivery Agent (CSA2001 Project 1)

## Overview
This project implements an autonomous delivery agent that navigates a 2D grid with:
- Static obstacles
- Varying terrain costs
- Dynamic moving obstacles

Implemented planners:
- BFS (uninformed, for unit-cost grids)
- Uniform-Cost Search (UCS)
- A* with Manhattan heuristic (admissible)
- Local search replanning example (simulated annealing)

## Deliverables in this repo
- Python source code (grid, search, local_search, visualization, agent, run_experiments, generate_maps)
- 4 maps (small, medium, large, dynamic)
- Experiment runner with logs + visualizations
- Report template (fill in results and export as PDF)
- Demo support with screenshots/visuals

## Installation
Python 3.8+ is recommended.

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\\Scripts\\activate     # Windows

pip install -r requirements.txt
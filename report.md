# Report — Autonomous Delivery Agent (CSA2001 Project 1)

## 1. Problem & Environment Model
The problem is to design an autonomous delivery agent that navigates a **2D grid city**.  
- **Grid cells** have integer costs ≥ 1.  
- **Obstacles** are impassable (value = 1).  
- **Terrain costs** (values >1) increase movement cost.  
- **Dynamic obstacles** move deterministically or unpredictably.  
- **Agent moves** in 4 directions (up, down, left, right).  

We use text-based maps to represent the environment, where `0` = free cell, `1` = obstacle, and integers >1 = terrain costs.

---

## 2. Agent Design
- **State representation**: `(row, col)` grid coordinates.  
- **Action space**: up, down, left, right (optional diagonals).  
- **Transition model**: moving into a cell adds its cost.  
- **Dynamic replanning**: agent detects new/moving obstacles and replans using local search (simulated annealing).  
- **Data structures**: priority queues for UCS/A*, deque for BFS.  

---

## 3. Algorithms Implemented
### BFS (Uninformed Search)
- Expands uniformly by levels.
- Works well in small, obstacle-heavy grids.
- Does not account for terrain cost.

### Uniform-Cost Search (UCS)
- Expands lowest-cost nodes first.
- Handles varying terrain costs.
- May expand more nodes than A* without a heuristic.

### A* Search
- Uses Manhattan distance as heuristic (admissible).
- Balances cost + heuristic, usually faster than UCS.

### Local Search (Simulated Annealing)
- Used for **replanning** when dynamic obstacles block path.
- Makes small modifications to an existing path to reduce cost.

---

## 4. Experimental Setup
- Maps:  
  - **Small** (10×10)  
  - **Medium** (20×20)  
  - **Large** (40×40)  
  - **Dynamic** (10×12 with moving obstacles)  
- Metrics collected:  
  - Path cost  
  - Path length  
  - Nodes expanded  
  - Runtime (seconds)  
- Hardware: (fill in your system specs here)  

---

## 5. Analysis & Conclusion
- **BFS**: good on small grids, fails with large/high-cost maps.  
- **UCS**: handles terrain well, but expands many nodes.  
- **A***: best trade-off, fastest in large grids.  
- **Local search**: useful for replanning in dynamic maps.  

**Conclusion**:  
- A* performs best overall in static maps.  
- UCS is reliable but slower.  
- BFS only suitable for trivial maps.  
- Replanning strategy allows handling dynamic environments effectively.  

---